from graphviz import Digraph

def create_process_map():
    process_map = Digraph(format='png', comment='Six Sigma Process Map for ARVAL Hackathon',
                          graph_attr={'rankdir': 'LR', 'splines': 'polyline'})

    # Define Nodes for DMAIC Phases
    process_map.node('Define', 'Define Phase', shape='box', style='filled', color='lightblue')
    process_map.node('Measure', 'Measure Phase', shape='box', style='filled', color='lightblue')
    process_map.node('Analyze', 'Analyze Phase', shape='box', style='filled', color='lightblue')
    process_map.node('Improve', 'Improve Phase', shape='box', style='filled', color='lightblue')
    process_map.node('Control', 'Control Phase', shape='box', style='filled', color='lightblue')

    # Define Process Steps for Each Phase
    # Define Phase
    process_map.node('D1', 'Identify objectives: Automate data extraction and ensure compliance')
    process_map.node('D2', 'Define problem statement: Time-consuming and error-prone processes')
    process_map.node('D3', 'Set project goals: Reduce processing time by 50%, ensure 95% accuracy')
    process_map.node('D4', 'Engage stakeholders: Define responsibilities and requirements')

    process_map.edge('Define', 'D1')
    process_map.edge('D1', 'D2')
    process_map.edge('D2', 'D3')
    process_map.edge('D3', 'D4')

    # Measure Phase
    process_map.node('M1', 'Collect data: Document processing times, error rates')
    process_map.node('M2', 'Baseline analysis: Current time per document, accuracy rates')
    process_map.node('M3', 'Identify KPIs: Time reduction, extraction accuracy, errors')

    process_map.edge('Measure', 'M1')
    process_map.edge('M1', 'M2')
    process_map.edge('M2', 'M3')

    # Analyze Phase
    process_map.node('A1', 'Perform root cause analysis: Use Fishbone diagram, Pareto analysis')
    process_map.node('A2', 'Map current process: Identify inefficiencies')
    process_map.node('A3', 'Validate findings: Compare manual and automated processes')

    process_map.edge('Analyze', 'A1')
    process_map.edge('A1', 'A2')
    process_map.edge('A2', 'A3')

    # Improve Phase
    process_map.node('I1', 'Develop automated pipeline: Azure Form Recognizer, data rules')
    process_map.node('I2', 'Test and refine pipeline: Pilot test with sample documents')
    process_map.node('I3', 'Incorporate feedback: Adjust logic based on validation results')
    process_map.node('I4', 'Document improvements: Update SOPs, process templates')

    process_map.edge('Improve', 'I1')
    process_map.edge('I1', 'I2')
    process_map.edge('I2', 'I3')
    process_map.edge('I3', 'I4')

    # Control Phase
    process_map.node('C1', 'Monitor process: Track performance via dashboards')
    process_map.node('C2', 'Validation framework: Periodic reviews, stakeholder feedback')
    process_map.node('C3', 'Sustain improvements: Ensure compliance, continuous feedback loop')

    process_map.edge('Control', 'C1')
    process_map.edge('C1', 'C2')
    process_map.edge('C2', 'C3')

    return process_map

# Generate Process Map
process_map = create_process_map()
file_path = '/mnt/data/six_sigma_process_map'
process_map.render(file_path, cleanup=True)
