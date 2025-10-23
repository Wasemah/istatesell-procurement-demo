#!/usr/bin/env python3
"""
iStateSell - Real Estate Procurement System
Main application runner

This is a proof-of-concept demo for portfolio purposes.
The original research remains confidential and unpublished.
"""

import os
import sys
from backend.cms_logic import RealEstateCMS
from backend.database import db
from backend.auth import auth

def display_banner():
    """Display a professional application banner"""
    banner = """
    ╔═══════════════════════════════════════════════╗
    ║              iStateSell Procurement           ║
    ║           Real Estate Management System       ║
    ║                 [DEMO VERSION]                ║
    ╚═══════════════════════════════════════════════╝
    
    🏗️  Streamlining Real Estate Procurement
    📊 Automated Quotation Generation
    💼 Portfolio Demonstration Project
    
    🔒 Note: This is a proof-of-concept demo
    """
    print(banner)

def initialize_system():
    """Initialize all system components"""
    print("🔧 Initializing iStateSell System...")
    
    # Initialize database
    try:
        db.initialize_database()
        print("✅ Database initialized")
    except Exception as e:
        print(f"⚠️  Database warning: {e}")
    
    # Create demo admin user
    auth.create_user("admin", "demo123", "admin")
    auth.create_user("manager", "demo123", "manager")
    print("✅ Demo users created (admin/demo123, manager/demo123)")
    
    return True

def run_demo_scenario():
    """Run a comprehensive demo scenario"""
    print("\n🎬 Starting Demo Scenario...")
    
    # Initialize CMS
    cms = RealEstateCMS()
    
    # Demo: Create projects
    print("\n📋 Creating Demo Projects...")
    projects = [
        ("Commercial Tower Dubai", 2500000, ["steel", "glass", "concrete", "elevators"]),
        ("Luxury Villa Project", 800000, ["marble", "smart_home", "landscaping"]),
        ("Office Complex", 1500000, ["furniture", "ac_systems", "security"])
    ]
    
    for name, budget, requirements in projects:
        project = cms.add_project(name, budget, requirements)
        print(f"   ✅ Created: {project['name']} (Budget: ${project['budget']:,})")
    
    # Demo: Generate quotations
    print("\n💰 Generating Sample Quotations...")
    
    # Sample vendor quotes for first project
    vendor_quotes = [
        {'vendor': 'SteelCo International', 'material': 'steel', 'quote': 450000},
        {'vendor': 'GlassTech Ltd', 'material': 'glass', 'quote': 320000},
        {'vendor': 'Concrete Masters', 'material': 'concrete', 'quote': 280000}
    ]
    
    quote = cms.generate_quote(1, vendor_quotes)
    
    print(f"   📊 Project: {quote['project_name']}")
    print(f"   💵 Total Estimated Cost: ${quote['total_estimated_cost']:,}")
    print(f"   📈 Budget Utilization: {(quote['total_estimated_cost']/quote['project_budget'])*100:.1f}%")
    
    # Display vendor breakdown
    print("\n   🏢 Vendor Breakdown:")
    for vq in quote['vendor_quotes']:
        print(f"      • {vq['vendor']}: ${vq['quote']:,}")
    
    return cms

def show_system_stats(cms):
    """Display system statistics"""
    print(f"\n📈 System Statistics:")
    print(f"   📂 Total Projects: {len(cms.projects)}")
    print(f"   👥 Registered Users: {len(auth.users)}")
    print(f"   💰 Total Project Budget: ${sum(p['budget'] for p in cms.projects):,}")

def interactive_demo():
    """Simple interactive demo mode"""
    print("\n🎯 Interactive Demo Mode")
    print("   Type 'projects' to list projects")
    print("   Type 'quote [id]' to generate quote for project")
    print("   Type 'exit' to end demo")
    
    cms = RealEstateCMS()
    
    # Pre-populate with demo data
    if not cms.projects:
        cms.add_project("Sample Project", 500000, ["materials", "labor"])
    
    while True:
        try:
            command = input("\niStateSell> ").strip().lower()
            
            if command == 'exit':
                break
            elif command == 'projects':
                print("\n📋 Current Projects:")
                for project in cms.projects:
                    print(f"   {project['id']}. {project['name']} (${project['budget']:,})")
            elif command.startswith('quote '):
                try:
                    project_id = int(command.split()[1])
                    sample_quotes = [
                        {'vendor': 'Demo Supplier', 'material': 'materials', 'quote': 250000},
                        {'vendor': 'Demo Contractor', 'material': 'labor', 'quote': 150000}
                    ]
                    quote = cms.generate_quote(project_id, sample_quotes)
                    print(f"   📄 Generated Quote: ${quote['total_estimated_cost']:,}")
                except (IndexError, ValueError):
                    print("   ❌ Usage: quote [project_id]")
            elif command == 'help':
                print("   Available commands: projects, quote [id], exit, help")
            else:
                print("   ❌ Unknown command. Type 'help' for options")
                
        except KeyboardInterrupt:
            print("\n\n👋 Demo ended by user")
            break

def main():
    """Main application entry point"""
    display_banner()
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--interactive':
            interactive_demo()
            return
        elif sys.argv[1] == '--init-only':
            initialize_system()
            return
    
    # Standard demo flow
    try:
        initialize_system()
        cms = run_demo_scenario()
        show_system_stats(cms)
        
        print(f"\n{'='*50}")
        print("🎉 Demo Completed Successfully!")
        print("💡 Tip: Run with '--interactive' for interactive mode")
        print("🔧 Tip: Run with '--init-only' to initialize database only")
        print(f"{'='*50}")
        
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        print("💡 Make sure all required files are in place")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
