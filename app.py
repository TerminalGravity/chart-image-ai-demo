# Imports
from pydantic import BaseModel, Field, conlist, confloat
import openai
import json
import os
import markdown

# Initialize OpenAI Client
openai.api_key = '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'
gpt_client = openai.GPT(model='gpt-4-1106-preview')

# Pydantic Model for Validation
class StockChartSummary(BaseModel):
    support_levels: conlist(confloat(gt=0), min_items=1) = Field(..., description="List of support levels with their price points")
    resistance_levels: conlist(confloat(gt=0), min_items=1) = Field(..., description="List of resistance levels with their price points")
    trend_direction: str = Field(..., description="Overall trend direction of the stock chart")
    chart_patterns: list[str] = Field(..., description="Identified chart patterns")
    technical_indicators: list[str] = Field(..., description="Key technical indicators observed in the chart")

# Function to Analyze Stock Chart Image
def analyze_stock_chart(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    response = gpt_client.create_image_summary(
        model='gpt-4-1106-preview',
        image=image_data,
        prompt="Analyze the stock chart."
    )
    return response

# Directory containing stock chart images
chart_image_dir = 'chart_images'
structured_output = {}
unstructured_output = {}

# Analyze each stock chart image
for image_file in os.listdir(chart_image_dir):
    if image_file.endswith('.png'):
        image_path = os.path.join(chart_image_dir, image_file)
        analysis_result = analyze_stock_chart(image_path)
        
        # Validate and save structured output
        try:
            validated_data = StockChartSummary.parse_obj(analysis_result.structured_data)
            structured_output[image_file] = validated_data.dict()
        except ValueError as e:
            print(f"Validation error for {image_file}: {e}")

        # Save unstructured output
        unstructured_output[image_file] = analysis_result.summary

# Save structured output to JSON file
with open('structured_output.json', 'w') as json_file:
    json.dump(structured_output, json_file, indent=4)

# Save unstructured output as Markdown file
with open('unstructured_output.md', 'w') as md_file:
    for image, summary in unstructured_output.items():
        md_file.write(f"## {image}\n\n")
        md_file.write(f"{markdown.markdown(summary)}\n\n")
