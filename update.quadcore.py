# Lily-gpt.ai always checks this file for AI Commits (All already have a censored and uncensored versions)
# Lastest stable version of right now is Tueson V1
# Main Models (Tueson-V1) - ( Lily Quantum 5 600K) ( Lily Quantum 5 750K ) 
# Beta Models (Tueson-V2) - ( Lily Tueson-v2 Quantum 6 950K )
# Beta Models (Tokenz-V1) - ( Tokenz-v1 Lily Quantum 7 1M ) 
# Beta Models (Tokenz-V2) - ( Tokenz-v2 Lily Quantum 8 15M )
# Beta Code Models (Tueson-V2) - ( Lily Tueson-v2 Quantum Code 6 950K )
# Beta Code Models (Tokenz-V1) - ( Tokenz-v1 Lily Quantum Code 7 1M )
# Beta Code Models (Tokenz-V2) - ( Tokenz-v2 Lily Quantum Code 8 15M )
# Code Models (Tueson-V1) - ( Lily Quantum 5 code 600K )
# LTE Models (Tueson-V1) - ( Lily Quantum 5 LTE 14K )


def check_latest_version(current_model):
    model_list = [
        # Main Models (Tueson-V1)
        "Lily Quantum 5 600K uncensored",
        "Lily Quantum 5 750K uncensored",
        "Lily Quantum 5 600K",
        "Lily Quantum 5 750K",
        
        # Beta Models (Tueson-V2)
        "Lily Tueson-v2 Quantum 6 950K uncensored",
        "Lily Tueson-v2 Quantum 6 950K",
        
        # Beta Models (Tokenz-V1)
        "Tokenz-v1 Lily Quantum 7 1M uncensored",
        "Tokenz-v1 Lily Quantum 7 1M",

        # Beta Models (Tokenz-V2)
        "Tokenz-v2 Lily Quantum 8 15M uncensored",
        "Tokenz-v2 Lily Quantum 8 15M",

        # Beta Code Models (Tueson-V2)
        "Lily Tueson-v2 Quantum Code 6 950K uncensored",
        "Lily Tueson-v2 Quantum Code 6 950K",

        # Beta Code Models (Tokenz-V1)
        "Tokenz-v1 Lily Quantum Code 7 1M uncensored",
        "Tokenz-v1 Lily Quantum Code 7 1M",

        # Beta Code Models (Tokenz-V2)
        "Tokenz-v2 Lily Quantum Code 8 15M uncensored",
        "Tokenz-v2 Lily Quantum Code 8 15M",

        # Code Models
        "Lily Quantum 5 code 600K uncensored",
        "Lily Quantum 5 code 600K",

        # LTE Models (uncensored and censored)
        "Lily Quantum 5 LTE 14K uncensored"
        "Lily Quantum 5 LTE 14K"
        
    ]

    if current_model not in model_list:
        print(f"Current model {current_model} not found in the list.")
        print("Simulating a fake download and applying a new model...")

        new_model = "Lily Quantum 5 600K"
        print(f"New model applied: {new_model}")

        return True

    else:
        print(f"Running {current_model}")
        return False

def add_repository(repo_url):
    print(f"Repository added: {repo_url}")

def main_chatbot():
    print("Running main Discord chatbot code...")

active = True

repository_url = "github.com/Project-LilyH47/lily-quadcore.ai"
add_repository(repository_url)

current_model = "Lily Quantum 5 600K"

if check_latest_version(current_model):
    exit()
    
print("Lily-gpt.ai up to date, Running discord bot")
main_chatbot()
