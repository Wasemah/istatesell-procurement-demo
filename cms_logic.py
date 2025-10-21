"""
iStateSell - Core CMS Logic Demo 
Proof-of-concept for real estate procurement system
"""

class RealEstateCMS:
  def _init_(self):
    self.projects = []
    self.vendors = []

 def add_project(self, name, budget, requirements):
   project = {
     'id' : len(self.projects) +,
    'name': name,
  'budget': budget,
     'requirement': requirements 
   }

self.projects.append(project)
print(f" ✅ Project '{name}' added successfully! ")
return project
