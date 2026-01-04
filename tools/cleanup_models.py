import os

# Milestones to keep for historical tracking
KEEP_ITERS = [1, 25, 50, 75, 100]
MODELS_DIR = "models"

def cleanup_models():
    if not os.path.exists(MODELS_DIR):
        print("Models directory not found.")
        return

    files = os.listdir(MODELS_DIR)
    deleted_count = 0
    
    for f in files:
        if f.startswith("checkpoint_iter_") and f.endswith(".pt"):
            try:
                # Extract iteration number
                iter_num = int(f.split("_")[-1].split(".")[0])
                if iter_num not in KEEP_ITERS:
                    os.remove(os.path.join(MODELS_DIR, f))
                    deleted_count += 1
            except ValueError:
                continue

    print(f"Cleanup complete. Deleted {deleted_count} intermediate models.")
    print(f"Kept milestones: {KEEP_ITERS}")

if __name__ == "__main__":
    cleanup_models()
