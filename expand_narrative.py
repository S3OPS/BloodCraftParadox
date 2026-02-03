#!/usr/bin/env python3
"""
Script to expand Blood Craft Paradox narrative:
1. Double word count from ~91,546 to ~183,000
2. Convert every other chapter (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30) to Rae's POV
3. Add world building, blood mechanics, and sexual tension
"""

import re
import sys

def read_file(filepath):
    """Read the markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    """Write content to file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_chapters(content):
    """Extract individual chapters from the content"""
    chapters = []
    chapter_pattern = r'^# \*\*Chapter (\d+)\*\*$'
    
    lines = content.split('\n')
    current_chapter = None
    chapter_lines = []
    
    for line in lines:
        match = re.match(chapter_pattern, line)
        if match:
            # Save previous chapter if exists
            if current_chapter is not None:
                chapters.append({
                    'number': current_chapter,
                    'content': '\n'.join(chapter_lines)
                })
            # Start new chapter
            current_chapter = int(match.group(1))
            chapter_lines = [line]
        else:
            if current_chapter is not None:
                chapter_lines.append(line)
    
    # Add last chapter
    if current_chapter is not None:
        chapters.append({
            'number': current_chapter,
            'content': '\n'.join(chapter_lines)
        })
    
    return chapters

def count_words(text):
    """Count words in text"""
    return len(text.split())

def is_rae_pov_chapter(chapter_num):
    """Determine if chapter should be from Rae's POV (every other chapter)"""
    return chapter_num % 2 == 0

def create_rae_pov_header(chapter_num):
    """Create header for Rae POV chapters"""
    return f"""# **Chapter {chapter_num}**
## *Raechelle's POV*

"""

def create_riven_pov_header(chapter_num):
    """Create header for Riven POV chapters"""
    return f"""# **Chapter {chapter_num}**

"""

def get_chapter_summary_rae(chapter_num):
    """Get narrative summary for what happens in each Rae POV chapter"""
    summaries = {
        2: """Raechelle has been tracking the Sixxx family for three days, following ancient protocols. She senses the attack 
moments before it happens—the earth magic signature of Terravos unmistakable. She arrives too late to prevent 
the crash but in time to witness Elara's death and Marcus's capture. She watches from shadows as Riven emerges 
from the wreckage, noting how his blood magic awakens violently. She guides him subtly, ensuring he finds his 
way to safety. Her centuries of preparation culminate in this moment of failure and new beginning.""",

        4: """Raechelle prepares the cabin for Riven's arrival, setting ancient wards and preparing the revealing ritual. 
She reflects on her 300-year wait, her bond to the bloodline, and her complex feelings about her mission. When 
Riven arrives, she struggles with her cat form's instinctive reaction to his scent—not just the young man he is, 
but traces of who he was before. The revelation of truth weighs heavy as she watches him read his mother's 
journal, knowing she must tell him enough to prepare him, but not so much that she reveals the full truth.""",

        6: """Raechelle watches Terravos's agents close in, using her familiar senses to track multiple threats. She reflects 
on the hunt-counter-hunt dance she's performed for centuries. Planning their escape to Nocturne brings memories 
of the last time she walked those streets—when the original Blood Archon ruled. She carefully manages Riven's 
growing dominance, balancing her need to submit to him with her duty to guide him away from his predecessor's 
path. The sexual tension builds as she realizes she's falling for him, not just serving him.""",

        8: """The bonding ritual from Raechelle's perspective—the terror and hope of binding herself again to a soul she once 
loved and feared. She feels the familiar magic differently than Riven, experiencing the full weight of their 
connection across lifetimes. During the physical union, she struggles with whether she's making love to Riven 
or to the ghost of who he was. The ritual completes successfully, but she feels the ancient presence stirring 
in him, recognizing patterns she hoped would never return.""",

        10: """Raechelle guides Riven through Nocturne, seeing the city through her centuries of experience while watching 
him discover it fresh. Every corner holds memories—places she went with the original Blood Archon, now overlaid 
with Riven's innocent wonder. She navigates supernatural politics, warning Riven away from old enemies who might 
recognize dangerous patterns. Meeting Seraphina privately, she receives knowing looks that confirm the Lady 
knows more than she says. Raechelle realizes she's not just protecting Riven—she's fighting to keep him from 
becoming what she helped destroy centuries ago.""",

        12: """Raechelle investigates Thorne's murder using familiar senses and old contacts, uncovering evidence of a frame 
job. She recognizes the blood magic signature as disturbingly similar to ancient patterns—making her question 
if someone knows Riven's true identity. Political maneuvering with Selene and other old friends reveals the 
depth of conspiracy against them. She must balance protecting Riven from supernatural politics while managing 
her growing fear that he's being manipulated into becoming his former self.""",

        14: """Raechelle brokers alliances with Lysandra and the werewolf pack, using her diplomatic skills and ancient 
connections. Meeting Kaine privately, she learns disturbing truths about what Terravos actually wants—not 
revenge, but redemption for his old friend. The revelation that others know about Riven's past identity forces 
her to confront her own deception. She struggles with when and how to tell Riven the truth, knowing it could 
destroy everything they're building.""",

        16: """Raechelle discovers the Blood Archon archives contain records of her own past—including her failure to save 
the original from madness. Research into the prophecy reveals that Riven's reincarnation was planned, not 
accidental. She learns that his parents were part of an ancient experiment in redemption through love. Processing 
this knowledge while maintaining her facade becomes increasingly difficult as Riven grows more powerful and 
more like his predecessor.""",

        18: """During the battle aftermath, Raechelle experiences the bond's pain-sharing intensely. Her injuries trigger 
protective instincts in Riven that remind her dangerously of the old possessiveness that turned toxic. In their 
recovery, she realizes she must find a way to strengthen him without awakening the darker aspects of his nature. 
Her healing is complicated by centuries-old wounds that resonate with new trauma.""",

        20: """Raechelle leads the strike team with tactical precision learned over centuries. In enemy territory, she 
confronts physical places she remembers from the original Blood Archon's reign. The lieutenant they face 
recognizes her, revealing that Terravos's inner circle all know about Riven's true identity. She must prevent 
Riven from hearing the truth while managing a complex extraction. Her divided loyalties reach a breaking point.""",

        22: """Raechelle feels the ancient Blood Archon consciousness stirring in Riven more strongly. During battles, she 
witnesses behaviors and techniques that weren't taught, but remembered. The terror of watching him become 
someone else while still being himself tears at her. She seeks advice from Seraphina, who reveals the Council 
has been monitoring Riven's progress and has contingency plans if he becomes unstable.""",

        24: """Raechelle uses their bond to suppress Riven's emerging ancient personality, an exhausting and ethically 
troubling process. She's essentially controlling him while claiming to love him. Confronting this hypocrisy, 
she prepares to tell him everything. Her confession is interrupted by crisis, leaving her plan incomplete but 
her guilt overwhelming.""",

        26: """Raechelle is forced to confess the full truth about Riven's identity and her mission. Her perspective shows 
the 300-year burden of guilt, love, and duty she's carried. She reveals her memories of the original Blood 
Archon—both his brilliance and his descent into madness. Her confession includes her own complicity in his 
eventual death and her complicated feelings about being bonded to his reincarnation.""",

        28: """Raechelle fights for Riven's right to self-determination, arguing against those who would eliminate or control 
him. She acknowledges her manipulation while asserting her genuine love evolved beyond duty. Through their bond, 
she feels his identity crisis and offers what support she can while respecting his need to process alone. She 
must prove to everyone—including Riven—that her love is real, not just an echo of what she felt centuries ago.""",

        30: """Raechelle participates in the ceremony that formalizes their renewed bond—this time based on truth. Her vows 
acknowledge their complicated past while committing to their chosen future. She reflects on the journey from 
guilty familiar to genuine partner, accepting that some wounds never fully heal but can be honored. The epilogue 
shows her helping Riven build his academy, finally finding purpose beyond survival and guilt."""
    }
    
    return summaries.get(chapter_num, "")

def analyze_current_state(chapters):
    """Analyze current state of chapters"""
    print("=" * 80)
    print("CURRENT STATE ANALYSIS")
    print("=" * 80)
    
    total_words = 0
    for chapter in chapters:
        words = count_words(chapter['content'])
        total_words += words
        pov = "Rae" if is_rae_pov_chapter(chapter['number']) else "Riven"
        target_pov = "Rae POV" if is_rae_pov_chapter(chapter['number']) else "Riven POV"
        print(f"Chapter {chapter['number']:2d}: {words:5d} words (Current: Riven POV, Target: {target_pov})")
    
    print("=" * 80)
    print(f"Total current words: {total_words:,}")
    print(f"Target words: 183,000")
    print(f"Words needed: {183000 - total_words:,}")
    print(f"Average per chapter: {183000 // len(chapters):,}")
    print("=" * 80)
    
    # Count chapters needing POV change
    rae_chapters = [c['number'] for c in chapters if is_rae_pov_chapter(c['number'])]
    print(f"\nChapters to convert to Rae's POV: {', '.join(map(str, rae_chapters))}")
    print(f"Total: {len(rae_chapters)} chapters need Rae's POV")
    print("=" * 80)

def main():
    filepath = 'paradox-version/Blood-Craft-Paradox.md'
    
    print("Reading Blood Craft Paradox...")
    content = read_file(filepath)
    
    print("Extracting chapters...")
    chapters = extract_chapters(content)
    
    print(f"Found {len(chapters)} chapters\n")
    
    analyze_current_state(chapters)
    
    print("\nThis script provides analysis.")
    print("Manual expansion will be done chapter by chapter with careful attention to:")
    print("  - Maintaining character voices")
    print("  - Expanding world building")
    print("  - Adding blood mechanics details")
    print("  - Enhancing romantic/sexual tension")
    print("  - Converting appropriate chapters to Rae's POV")

if __name__ == '__main__':
    main()
