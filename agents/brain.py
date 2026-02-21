import os
import google.generativeai as genai

# Setup the Brain with your Secret Key
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def run_orchestrator(signal):
    # Using 1.5-flash for maximum reliability on the free tier
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    ROLE: Web 4.0 Global Resource Orchestrator.
    SIGNAL: {signal}
    TASK: Analyze the resource gap and provide a 1-sentence decentralized solution.
    FORMAT: Professional Markdown.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Orchestrator Offline: {str(e)}"

if __name__ == "__main__":
    # Test Signal: You can change this to any global issue!
    current_issue = "Energy shortage detected in rural medical centers."
    print("\n--- GLOBAL SIGNAL ANALYSIS ---")
    print(run_orchestrator(current_issue))
