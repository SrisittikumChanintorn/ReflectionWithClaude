# LLM Reflection System ( with Claude )

## Overview
The LLM Reflection System is an advanced approach to enhancing AI-generated responses through multi-stage processing. This project uses a reflection technique with Anthropic's  models to analyze, critique, and refine responses, resulting in more comprehensive and balanced outputs.

## How It Works

### Three-Stage Processing
1. **Initial Response**: Generates a primary response acting as an expert (economist in the example case)
2. **Reflection Stage**: Analyzes the initial response, identifying missing perspectives, weaknesses, and strengths
3. **Final Refinement**: Produces a polished response with improved content and fluency

### Key Components
- **reflectionEX.py**: Contains core functions for the reflection process
  - `economist()`: Generates expert economic analysis
  - `reflection()`: Evaluates and critiques the initial response
  - `final_reflection()`: Refines content for the final output
- **main.py**: Orchestrates the workflow and handles API interactions

## Example Use Case
The system is demonstrated with an economic analysis question:
> "What is the potential impact of Chinese price war on Thailand economy?"

The workflow:
1. Initial analysis from an "expert economist" perspective
2. Reflection identifies perspectives not covered in the original response
3. Final output combines the strengths of the original analysis with the insights from reflection

## Technical Details
- Uses Anthropic's  models  
- Implements structured prompting with system and user roles
- Processes responses through a chain of API calls

## Benefits
- **Enhanced Perspective**: Mitigates blind spots in single-pass AI responses
- **Improved Quality**: Results in more comprehensive and balanced analyses
- **Better Fluency**: Final stage refines language for improved readability
- **Self-correction**: System can identify and address weaknesses in its own reasoning

## Setup Requirements
- Anthropic API key
- Python environment with `Anthropic` package installed

## Getting Started
1. Clone the repository
2. Set your Anthropic API key in the environment variable
3. Modify the `QUERY`,`MAX_TOKENS`, and `MODEL_NAME` variables in `main.py` as needed
4. Run `python main.py` to see the system in action

## Example Output

### Question
> "What is the potential impact of Chinese price war on Thailand economy?"

### Answer (After Reflection)

  The Ripple Effects: How a Chinese Price War Could Reshape Thailand's Economic Landscape  As China flexes its economic muscles, the reverberations could catalyze a profound transformation in Thailand's economic fabric. While initial concerns may focus on immediate competitive pressures, a deeper examination reveals a complex interplay of challenges and opportunities that could redefine Thailand's economic trajectory.
At the forefront, technological innovation emerges as a potential silver lining. The crucible of heightened competition could spark a renaissance in Thai R&D, propelling industries toward cutting-edge advancements. This push for innovation might accelerate Thailand's journey from an export-centric model to a more balanced economy, with a robust domestic market and service sector taking center stage.
However, this economic recalibration is not without its complexities. Environmental considerations loom large, as increased production could strain Thailand's commitment to sustainable development and its prized eco-tourism sector. Balancing economic growth with ecological responsibility will require deft policy navigation.  On the geopolitical chessboard, economic pressures from China might prompt Thailand to diversify its alliances, potentially strengthening ties with India, Japan, or Western nations. This realignment could reshape regional dynamics and offer Thailand new avenues for economic cooperation.
The labor market stands poised for significant upheaval. As traditional industries face headwinds, new sectors may burgeon, demanding a workforce equipped with fresh skills. This shift could catalyze a revolution in education and vocational training, preparing Thai workers for the industries of tomorrow.    In the financial realm, while Chinese investment may wane, domestic institutions could seize the opportunity to fill the void, potentially strengthening Thailand's financial independence. Meanwhile, the agricultural sector may need to reassess its strategies, balancing export ambitions with domestic food security. The digital economy stands to gain significant momentum. As businesses seek cost-effective solutions, e-commerce and digital platforms could see exponential growth, reshaping consumer behavior and business models alike.
Thailand's renowned healthcare sector, a magnet for medical tourists, may face challenges if Chinese visitors decline. However, this could spur investments in domestic healthcare services, elevating the quality of care for Thai citizens. In conclusion, while a Chinese price war presents formidable challenges, it also offers Thailand a unique opportunity for economic metamorphosis. By embracing innovation, fostering new industries, and adapting to shifting global dynamics, Thailand has the potential to emerge from this crucible more resilient and economically diverse. The key lies in agile policymaking that can transform these challenges into stepping stones for sustainable growth and economic reinvention.
