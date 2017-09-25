#for each star we compare each magnitude for each catalogue to the master magnitude and plot a graph
for i in range(1, no_files):

	#calculating the variability and the offset
	delta_mag = magnitude_table[:,i] - magnitude_table[:,0]
	delta_mag_avg = np.nanmean(delta_mag)
	offset_delta_mag = delta_mag - delta_mag_avg

	#applying a 3rd degree polynomial fit using a Savitsky Golay filter
	filter_mag = savgol_filter(np.nan_to_num(offset_delta_mag), 651 , 3)
	fitted_mag = offset_delta_mag - filter_mag

	#here is where the graphs are plotted
	plt.plot(magnitude_table[:,0], delta_mag, 'ro')
	#plt.plot(magnitude_table[:,0], offset_delta_mag, 'bo')
	plt.plot(magnitude_table[:,0], fitted_mag, 'bo')

	plt.ylabel("m" +str(i+1) + " - m1")
	plt.xlabel("m1")
	plt.savefig('images/truncated_distribution/fitted_distribution_%s.png' % i)
	plt.show()
	plt.clf()