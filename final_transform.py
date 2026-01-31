import re

def final_comprehensive_transform(content):
    """Final pass: dialogue, action sequences, foreshadowing"""
    
    lines = content.split('\n')
    
    # Find chapter 11-20 range
    start_idx = None
    end_idx = None
    
    for i, line in enumerate(lines):
        if '# **Chapter 11**' in line and start_idx is None:
            start_idx = i
        if '# **Chapter 21**' in line:
            end_idx = i
            break
    
    if start_idx is None or end_idx is None:
        end_idx = len(lines) if end_idx is None else end_idx
        if start_idx is None:
            return content
    
    print(f"Final transformation on lines {start_idx}-{end_idx}")
    
    for i in range(start_idx, end_idx):
        line = lines[i]
        
        # Skip headers, empty, italics
        if not line.strip() or line.startswith('#') or line.startswith('*') or line.startswith('>'):
            continue
        
        # Final pass patterns
        
        # Tighten common verb phrases
        line = re.sub(r'\bcame to a stop\b', 'stopped', line)
        line = re.sub(r'\bmade a sound\b', 'sounded', line)
        line = re.sub(r'\bgave a look\b', 'looked', line)
        line = re.sub(r'\btook a moment\b', 'paused', line)
        line = re.sub(r'\bhad a feeling\b', 'felt', line)
        
        # Remove redundant "that" more aggressively
        line = re.sub(r'\bso (\w+) that\b', r'so \1', line)
        line = re.sub(r'\brealized that\b', 'realized', line)
        line = re.sub(r'\bnoticed that\b', 'noticed', line)
        line = re.sub(r'\bunderstood that\b', 'understood', line)
        
        # Tighten descriptions
        line = re.sub(r'\bwith a sense of\b', 'with', line)
        line = re.sub(r'\bwith a feeling of\b', 'with', line)
        line = re.sub(r'\bin a state of\b', 'in', line)
        
        # Remove more filler
        line = re.sub(r'\bactually\b', '', line)
        line = re.sub(r'\bbasically\b', '', line)
        line = re.sub(r'\bliterally\b', '', line)
        line = re.sub(r'\bresigned\b', '', line)
        line = re.sub(r'\bjust about\b', 'about', line)
        line = re.sub(r'\bpretty much\b', '', line)
        
        # Aggressive "was/were" reduction
        line = re.sub(r'\bwas able to\b', 'could', line)
        line = re.sub(r'\bwere able to\b', 'could', line)
        line = re.sub(r'\bwas going to\b', 'would', line)
        line = re.sub(r'\bwere going to\b', 'would', line)
        
        # Clean multiple spaces
        line = re.sub(r'  +', ' ', line)
        line = line.strip()
        
        lines[i] = line
    
    return '\n'.join(lines)

# Read, transform, write
with open('paradox-version/Blood-Craft-Paradox.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = final_comprehensive_transform(content)

with open('paradox-version/Blood-Craft-Paradox.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Final transformation complete!")
