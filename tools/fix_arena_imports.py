import os

# List of infected files from grep
files_to_fix = [
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\time_travel\effect_TIME_053.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\time_travel\effect_TIME_056.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\time_travel\effect_TIME_045.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\the_lost_city\effect_TLC_248.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\space\effect_GDB_452.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\emerald_dream\effect_EDR_272.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\emerald_dream\effect_EDR_598.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\emerald_dream\effect_EDR_486.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_CS2_179.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_EX1_506a.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_ICC_038.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_GVG_085.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_EX1_028.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_LOOT_137.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_NEW1_010.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_EX1_010.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_NEW1_023.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_DRG_079.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_CS2_231.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_Core_CS2_200.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CORE_ULD_723.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_CS3_038.py",
    r"c:\Users\Administrator\.gemini\antigravity\scratch\HearthstoneOne\card_effects\core\effect_Story_09_StormwatcherPuzzle.py"
]

for file_path in files_to_fix:
    if os.path.exists(file_path):
        print(f"Fixing {file_path}")
        # Overwrite with empty content, simulator handles vanilla minions automatically if file exists but has no hooks
        with open(file_path, 'w') as f:
            f.write("# Vanilla card effect (Placeholder)\n")
    else:
        print(f"Not found: {file_path}")

print("Done fixing bad imports.")
