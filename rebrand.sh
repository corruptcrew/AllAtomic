#!/bin/bash

# Rebrand HellBot to AllAtomic
cd /mnt/data/openclaw/workspace/.openclaw/workspace/AllAtomic/Hellbot

# Replace HellBot references with AllAtomic
find . -type f -name "*.py" -exec sed -i 's/HellBot/AllAtomic/g' {} \;
find . -type f -name "*.py" -exec sed -i 's/hellbot/AllAtomic/g' {} \;
find . -type f -name "*.py" -exec sed -i 's/HellBot/AllAtomic/g' {} \;
find . -type f -name "*.py" -exec sed -i 's/The-HellBot/corruptcrew/g' {} \;
find . -type f -name "*.py" -exec sed -i 's/@HellBot/@GhostMarshal/g' {} \;

# Replace file names
mv HellBot.log AllAtomic.log 2>/dev/null || true

echo "Rebranding complete!"
