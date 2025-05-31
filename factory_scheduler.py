import pandas as pd
import pulp

jobs = {'Job1', 'Job2', 'Job3', 'Job4', 'Job5'}
machines = {'Machine1', 'Machine2'}
processing_times = {
    ('Job1', 'Machine1'): 2,
    ('Job1', 'Machine2'): 3,
    ('Job2', 'Machine1'): 4,
    ('Job2', 'Machine2'): 1,
    ('Job3', 'Machine1'): 3,
    ('Job3', 'Machine2'): 2,
    ('Job4', 'Machine1'): 5,
    ('Job4', 'Machine2'): 4,
    ('Job5', 'Machine1'): 2,
    ('Job5', 'Machine2'): 3
}

prob = pulp.LpProblem("Factory_Scheduling", pulp.LpMinimize)
jobvar = pulp.LpVariable.dicts("assign", (jobs, machines), 0, 1, pulp.LpBinary)
prob+=pulp.lpSum(processing_times[j,m] * jobvar[j][m] for j in jobs for m in machines), "Total_Processing_Time"
for j in jobs:
    prob += pulp.lpSum(jobvar[j][m] for m in machines) == 1, f"Job_{j}_Assigned_Once"

prob.solve()
# Display results
print("Status:", pulp.LpStatus[prob.status])
for j in jobs:
    for m in machines:
        if jobvar[j][m].varValue > 0:
            print(f"{j} is assigned to {m} with processing time {processing_times[(j, m)]}")
# Convert results to a DataFrame
results = []
for j in jobs:
    for m in machines:
        if jobvar[j][m].varValue > 0:
            results.append({
                'Job': j,
                'Machine': m,
                'Processing Time': processing_times[(j, m)],
                'Assigned': jobvar[j][m].varValue
            })
results_df = pd.DataFrame(results)
# Display the DataFrame
print("\nResults DataFrame:")
print(results_df)
# Save the DataFrame to a CSV file
results_df.to_csv('factory_scheduling_results.csv', index=False)