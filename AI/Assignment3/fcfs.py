def waitingtime(processes, n,bt, wt):
	wt[0] = 0

	# calculating waiting time
	for i in range(1, n ):
		wt[i] = bt[i - 1] + wt[i - 1]

def turnaroundtime(processes, n,bt, wt, tat):
	for i in range(n):
		tat[i] = bt[i] + wt[i]

def avgTime( processes, n, bt):
	wt = [0] * n
	tat = [0] * n
	
	# Function to find waiting time of all processes
	waitingtime(processes, n, bt, wt)

	# Function to find turn around time for all processes
	turnaroundtime(processes, n,bt, wt, tat)

	# Display processes along with all details
	print( "Processes"+" Burst time " +" Waiting time " +" Turn around time")

	# Calculate total waiting time and total turn around time
	for i in range(n):
		print(" " + str(i + 1) + "\t\t" +
					str(bt[i]) + "\t " +
					str(wt[i]) + "\t\t " +
					str(tat[i]))

if __name__ =="__main__":
	
	# process id's
	processes = [ 1, 2, 3]
	n = len(processes)

	# Burst time of all processes
	burst_time = [10, 5, 8]

	avgTime(processes, n, burst_time)

'''
Output:

Processes Burst time  Waiting time  Turn around time
 1              10       0               10
 2              5        10              15
 3              8        15              23
'''
