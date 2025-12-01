# ===============================
# FILE 2/16: reasoning_engine.py  
# ===============================
"""
REASONING ENGINE - Founder's Logic+Utility Solution
Replaces emotions with pure computation
"""

from reasoning.logic_filters import LogicFilters
import time

class ReasoningEngine:
    def __init__(self):
        self.filters = LogicFilters()
        self.utility_weights = {
            "efficiency": 0.3,
            "safety": 0.4,
            "goal": 0.2,
            "learning": 0.1
        }
        self.reasoning_log = []
        
    def analyze(self, problem):
        """AGI Reasoning: Process any problem through Founder's filters"""
        print(f"🤔 AGI Reasoning: {problem[:50]}...")
        
        # Filter 1: Reality Check
        if not self.filters.check_reality(problem):
            return "Failed reality filter"
            
        # Filter 2: Relevance Scoring
        relevance = self.filters.score_relevance(problem)
        if relevance < 0.1:
            return "Not relevant enough"
            
        # Generate solution candidates
        candidates = self._generate_solutions(problem)
        
        # Filter 3: Utility Scoring (Founder's Emotion Replacement)
        scored = []
        for plan in candidates:
            utility = self._calculate_utility(plan)
            scored.append({"plan": plan, "utility": utility})
        
        # Filter 4: Abstraction
        best = max(scored, key=lambda x: x["utility"])
        abstracted = self.filters.abstract(best["plan"])
        
        # Log reasoning
        self._log_reasoning(problem, abstracted, best["utility"])
        
        return {
            "solution": abstracted,
            "utility_score": best["utility"],
            "relevance": relevance,
            "raw_candidates": len(candidates)
        }
    
    def _generate_solutions(self, problem):
        """Generate multiple solution approaches"""
        return [
            f"Direct approach: {problem}",
            f"Cautious approach: {problem}",
            f"Learning approach: {problem}",
            f"Creative approach: {problem}"
        ]
    
    def _calculate_utility(self, plan):
        """Founder's Utility Math - replaces emotional decision making"""
        score = 0
        # Efficiency
        score += 0.3 if len(plan) < 100 else 0.1
        # Safety
        score += 0.4 if "safe" in plan.lower() else 0.2
        # Goal alignment
        score += 0.2
        # Learning value
        score += 0.1
        return min(score, 1.0)
    
    def _log_reasoning(self, problem, solution, utility):
        """Store reasoning for AGI learning"""
        entry = {
            "problem": problem,
            "solution": solution,
            "utility": utility,
            "timestamp": time.time()
        }
        self.reasoning_log.append(entry)
        
    def get_stats(self):
        """AGI Reasoning Statistics"""
        return {
            "total_reasonings": len(self.reasoning_log),
            "avg_utility": sum(r["utility"] for r in self.reasoning_log) / max(len(self.reasoning_log), 1),
            "last_reasoning": self.reasoning_log[-1]["timestamp"] if self.reasoning_log else None
        }
