"""
iStateSell - Core CMS Logic Demo
Proof-of-concept for real estate procurement system
"""

class RealEstateCMS:
    def __init__(self):
        self.projects = []
        self.vendors = []
    
    def add_project(self, name, budget, requirements):
        project = {
            'id': len(self.projects) + 1,
            'name': name,
            'budget': budget,
            'requirements': requirements
        }
        self.projects.append(project)
        print(f"✅ Project '{name}' added successfully!")
        return project
    
    def generate_quote(self, project_id, vendor_quotes):
        """Generate a structured quotation for a project"""
        project = next((p for p in self.projects if p['id'] == project_id), None)
        
        if not project:
            return "❌ Project not found"
        
        quote = {
            'project_name': project['name'],
            'project_budget': project['budget'],
            'vendor_quotes': vendor_quotes,
            'total_estimated_cost': sum(vq['quote'] for vq in vendor_quotes)
        }
        
        return quote

# Demo execution
if __name__ == "__main__":
    cms = RealEstateCMS()
    cms.add_project("Commercial Tower", 500000, ["cement", "steel", "glass"])
    
    sample_quotes = [
        {'vendor': 'ABC Supplies', 'material': 'cement', 'quote': 50000},
        {'vendor': 'XYZ Steel', 'material': 'steel', 'quote': 150000}
    ]
    
    quote = cms.generate_quote(1, sample_quotes)
    print("📊 Generated Quote:", quote)
