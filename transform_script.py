import re

def transform_blood_craft(content):
    """Apply transformation rules to Blood Craft Paradox chapters 11-20"""
    
    # Split into lines
    lines = content.split('\n')
    
    # Find chapter 11 start (around line 3616) and chapter 20 end (around line 6351)
    start_idx = None
    end_idx = None
    
    for i, line in enumerate(lines):
        if '# **Chapter 11**' in line and start_idx is None:
            start_idx = i
        if '# **Chapter 21**' in line and end_idx is None:
            end_idx = i
            break
    
    if start_idx is None:
        print("Could not find Chapter 11 start")
        return content
    
    if end_idx is None:
        end_idx = len(lines)
    
    print(f"Transforming lines {start_idx} to {end_idx}")
    
    # Process each line in target range
    for i in range(start_idx, end_idx):
        line = lines[i]
        original = line
        
        # Skip chapter headers and empty lines
        if line.startswith('#') or not line.strip():
            continue
        
        # Transform patterns
        
        # Remove unnecessary words in descriptions
        line = re.sub(r'\bseemed to be\b', 'seemed', line)
        line = re.sub(r'\bappeared to be\b', 'appeared', line)
        line = re.sub(r'\bhappened to be\b', 'was', line)
        line = re.sub(r'\bmanaged to\b', '', line)
        line = re.sub(r'\btried to\b', 'tried', line)
        line = re.sub(r'\bstarted to\b', 'started', line)
        line = re.sub(r'\bbegan to\b', 'began', line)
        line = re.sub(r'\bcontinued to\b', 'continued', line)
        
        # Tighten "was/were" constructions
        line = re.sub(r'\bI was feeling\b', 'I felt', line)
        line = re.sub(r'\bshe was feeling\b', 'she felt', line)
        line = re.sub(r'\bhe was feeling\b', 'he felt', line)
        line = re.sub(r'\bwas filled with\b', 'filled with', line)
        
        # Remove filter words
        line = re.sub(r'\bI could sense\b', 'I sensed', line)
        line = re.sub(r'\bI could tell\b', 'I knew', line)
        
        # Tighten prepositional phrases
        line = re.sub(r'\bin the process of\b', 'was', line)
        line = re.sub(r'\bin the middle of\b', 'was', line)
        line = re.sub(r'\bin the act of\b', 'was', line)
        
        # Remove redundant descriptors  
        line = re.sub(r'\bcompletely and utterly\b', 'completely', line)
        line = re.sub(r'\beach and every\b', 'every', line)
        line = re.sub(r'\bfirst and foremost\b', 'first', line)
        line = re.sub(r'\bvarious different\b', 'various', line)
        line = re.sub(r'\bunexpected surprise\b', 'surprise', line)
        
        # Tighten dialogue tags
        line = re.sub(r'she said (\w+ly)', r'she said. \1', line)
        line = re.sub(r'he said (\w+ly)', r'he said. \1', line)
        line = re.sub(r'I said (\w+ly)', r'I said. \1', line)
        
        # Replace weak verbs
        line = re.sub(r'\bmade my way to\b', 'went to', line)
        line = re.sub(r'\bmade a decision to\b', 'decided to', line)
        line = re.sub(r'\bgave a nod\b', 'nodded', line)
        line = re.sub(r'\bgave a smile\b', 'smiled', line)
        line = re.sub(r'\btook a step\b', 'stepped', line)
        line = re.sub(r'\btook a breath\b', 'breathed', line)
        line = re.sub(r'\blet out a sigh\b', 'sighed', line)
        
        # Clean up double spaces that might have been created
        line = re.sub(r'  +', ' ', line)
        line = line.strip()
        
        if line != original:
            lines[i] = line
    
    return '\n'.join(lines)

# Read file
with open('paradox-version/Blood-Craft-Paradox.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Transform
transformed = transform_blood_craft(content)

# Write back
with open('paradox-version/Blood-Craft-Paradox.md', 'w', encoding='utf-8') as f:
    f.write(transformed)

print("Transformation complete")
