## Imports

# from pydantic import BaseModel, Field, conlist, confloat
# OpenAI, LangChain, ... 


## Init OpenAI Clients
# gpt-4-1106-preview=llm



# ## Init gpt prompts on the .png images in the folder 'chart_images' 
# ##prompt 1
# """Analyze the attached image of a stock chart. Identify and list all horizontal lines representing support and resistance levels, along with their corresponding price points. Additionally, provide an overall summary of the chart's trend direction, any visible chart patterns, and key technical indicators. Structure this information as follows: support levels, resistance levels, trend direction, chart patterns, and technical indicators."""
# ##prompt 2
# """
# Examine the stock chart in the attached image, paying special attention to the horizontal lines marking support and resistance. List each level with its price and indicate whether it is a support or resistance level. Also, describe the general trend of the stock and note any significant chart patterns or indicators. Organize the output in a structured manner with clear headings for each category.
# """
# ##prompt3
# """
# Review the provided stock chart image and compare it with standard chart patterns. Identify and list the support and resistance levels, noting their price points. Assess the overall trend and predict potential future movements based on the chart's current pattern. Structure your analysis with sections for support and resistance levels, trend assessment, and predictive insights.
# """
## Init the validation steps
# class StockChartSummary(BaseModel):
# "Validate the following structured output using the 'StockChartSummary' Pydantic model. Ensure that each support and resistance level is a positive number and correctly categorized, and that the trend direction, chart patterns, and technical indicators are accurately described."


# Run the service 
# Save strutured output responses as structured JSON:
    # support_levels: 
    # resistance_levels: 
    # trend_direction:
    # chart_patterns: 
    # technical_indicators:



# Save unstructured output as formatted MD file:
# Comprehensive Analysis response:
# Specific Feature Focus response:
# Predictive Analysis response:
