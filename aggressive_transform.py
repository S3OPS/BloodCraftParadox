import re

def aggressively_transform(content):
    """Apply aggressive Stephen King-style transformations"""
    
    lines = content.split('\n')
    
    # Find chapters 15-20
    in_target = False
    start_idx = None
    end_idx = None
    
    for i, line in enumerate(lines):
        if '# **Chapter 15**' in line:
            in_target = True
            start_idx = i
        elif '# **Chapter 21**' in line or i == len(lines) - 1:
            end_idx = i
            break
    
    if start_idx is None:
        return content
    
    if end_idx is None:
        end_idx = len(lines)
    
    print(f"Transforming chapters 15-20 (lines {start_idx} to {end_idx})")
    
    for i in range(start_idx, end_idx):
        line = lines[i]
        
        # Skip headers, empty lines, italics
        if not line.strip() or line.startswith('#') or line.startswith('*'):
            continue
        
        # Aggressive simplification patterns
        
        # Remove "the" in many cases (keep for proper nouns)
        line = re.sub(r'\binto the\b', 'into', line)
        line = re.sub(r'\bfrom the\b', 'from', line)
        line = re.sub(r'\bat the\b', 'at', line)
        line = re.sub(r'\bto the\b', 'to', line)
        line = re.sub(r'\bof the\b', 'of', line)
        line = re.sub(r'\bon the\b', 'on', line)
        
        # Remove filler
        line = re.sub(r'\bI found myself\b', 'I', line)
        line = re.sub(r'\bI could feel myself\b', 'I felt', line)
        line = re.sub(r'\bseemed to\b', 'seemed', line)
        line = re.sub(r'\bappeared to\b', 'appeared', line)
        line = re.sub(r'\bas if\b', 'like', line)
        line = re.sub(r'\bin order to\b', 'to', line)
        
        # Aggressive verb tightening
        line = re.sub(r'\bhad been\b', 'was', line)
        line = re.sub(r'\bhave been\b', 'were', line)
        line = re.sub(r'\bwould be\b', 'was', line)
        line = re.sub(r'\bmight be\b', 'was', line)
        
        # Remove hedge words
        line = re.sub(r'\bsomewhat\b', '', line)
        line = re.sub(r'\bslightly\b', '', line)
        line = re.sub(r'\ba bit\b', '', line)
        line = re.sub(r'\ba little\b', '', line)
        line = re.sub(r'\bkind of\b', '', line)
        line = re.sub(r'\bsort of\b', '', line)
        
        # Fix double spaces
        line = re.sub(r'  +', ' ', line)
        line = line.strip()
        
        lines[i] = line
    
    return '\n'.join(lines)

# Read and transform
with open('paradox-version/Blood-Craft-Paradox.md', 'r', encoding='utf-8') as f:
    content = f.read()

transformed = aggressively_transform(content)

with open('paradox-version/Blood-Craft-Paradox.md', 'w', encoding='utf-8') as f:
    f.write(transformed)

print("Aggressive transformation complete")
