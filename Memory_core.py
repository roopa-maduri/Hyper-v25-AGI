# ===============================
# FILE 4/16: memory_core.py
# ===============================
"""
MEMORY CORE - Founder's Data Solution
AGI needs memory to learn and improve
"""

import json
import time
from collections import defaultdict

class MemoryCore:
    def __init__(self, filepath="memory/memory_index.json"):
        self.filepath = filepath
        self.memories = defaultdict(list)
        self.load()
        
    def store(self, memory_type, data):
        """AGI Memory Storage"""
        entry = {
            "data": data,
            "type": memory_type,
            "timestamp": time.time(),
            "access_count": 0
        }
        self.memories[memory_type].append(entry)
        self.save()
        return True
        
    def retrieve(self, memory_type, count=5):
        """AGI Memory Retrieval"""
        if memory_type not in self.memories:
            return []
            
        memories = self.memories[memory_type][-count:]
        for mem in memories:
            mem["access_count"] += 1
            
        return memories
        
    def search(self, query):
        """AGI Memory Search"""
        results = []
        query_lower = query.lower()
        
        for mem_type, entries in self.memories.items():
            for entry in entries:
                if query_lower in str(entry["data"]).lower():
                    results.append(entry)
                    
        return sorted(results, key=lambda x: x["timestamp"], reverse=True)
        
    def learn_pattern(self, experiences):
        """AGI Pattern Learning"""
        patterns = {}
        for exp in experiences[-10:]:  # Last 10 experiences
            data_str = str(exp["data"])
            patterns[data_str[:50]] = patterns.get(data_str[:50], 0) + 1
            
        self.store("learned_patterns", patterns)
        return patterns
        
    def save(self):
        """Save AGI Memory"""
        try:
            with open(self.filepath, 'w') as f:
                json.dump(dict(self.memories), f, indent=2)
        except:
            print("Memory save failed - continuing")
            
    def load(self):
        """Load AGI Memory"""
        try:
            with open(self.filepath, 'r') as f:
                loaded = json.load(f)
                self.memories.update(loaded)
        except:
            print("No existing memory - starting fresh")
            
    def stats(self):
        """AGI Memory Statistics"""
        total = sum(len(entries) for entries in self.memories.values())
        return {
            "total_memories": total,
            "memory_types": list(self.memories.keys()),
            "oldest": min([e["timestamp"] for entries in self.memories.values() for e in entries]) if total > 0 else 0,
            "newest": max([e["timestamp"] for entries in self.memories.values() for e in entries]) if total > 0 else 0
        }
