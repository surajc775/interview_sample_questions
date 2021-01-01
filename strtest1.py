
target_ps = []
target_as = []
target_ts = []
target_hs = []
target_a2s = []
target_is = []
qry_idxs = []


def pattern(test_str, queries):

	print("Input:")
	print(test_str)
	print(len(queries))
	print(queries)

	global target_ps
	global target_as
	global target_ts
	global target_hs
	global target_a2s
	global target_is
	global qry_idxs


	result = []
	target = 'pathai'
	temp1 = []
	temp2 = []
	temp3 = []
	temp4 = []
	temp5 = []
	temp6 = []

	char_counter = 0
	t_len = len(test_str)
	print(t_len)

	for char in test_str:
		if (char == target[0]):
			target_ps.append(char_counter)
			if (char_counter != 0):
				temp1.append(char_counter - t_len)
		if (char == target[1]):
			target_as.append(char_counter)
			target_a2s.append(char_counter)
			if (char_counter != 0):
				temp2.append(char_counter - t_len)
				temp5.append(char_counter - t_len)
		if (char == target[2]):
			target_ts.append(char_counter)
			if (char_counter != 0):
				temp3.append(char_counter - t_len)
		if (char == target[3]):
			target_hs.append(char_counter)
			if (char_counter != 0):
				temp4.append(char_counter - t_len)
		if (char == target[5]):
			target_is.append(char_counter)
			if (char_counter != 0):
				temp6.append(char_counter - t_len)
		char_counter += 1

	target_ps = target_ps + temp1
	target_as = target_as + temp2
	target_ts = target_ts + temp3
	target_hs = target_hs + temp4
	target_a2s = target_a2s + temp5
	target_is = target_is + temp6
	print(target_ps)

	for query in queries:
		start = query[0]
		end = query[1]

		qry_idxs.clear()
		for idx in range(start, end+1):
			qry_idxs.append(idx)

		print(qry_idxs)
		target_ps.reverse()
		#target_as.reverse()
		#target_ts.reverse()
		#target_hs.reverse()
		#target_a2s.reverse()
		#target_is.reverse()
		start_idx = 0
		end_idx = 0
		found = False

		for p_val in target_ps:
			if p_val not in qry_idxs:
				continue

			start_idx = p_val
			print('start', start_idx)
			found = True

			end_idx = check_alist(p_val)
			print('end', end_idx)

			if (end_idx > 0):
				break
			else:
				found = False
				start_idx = 0

		print('start', start_idx)
		print('end', end_idx)
		if (found):
			result.append(end_idx - start_idx + 1)
		else:
			result.append(0)


	return result


def check_alist(val):
	a_idx = 0

	for a_val in target_as:
		if (a_val <= val):
			continue

		if a_val not in qry_idxs:
			continue

		a_idx = check_tlist(a_val)
		print('a idx', a_idx)

		if (a_idx > 0):
			break

	return a_idx


def check_tlist(val):
	t_idx = 0

	for t_val in target_ts:
		if (t_val <= val):
			continue
		
		if t_val not in qry_idxs:
			continue

		t_idx = check_hlist(t_val)
		print('t idx', t_idx)

		if (t_idx > 0):
			break

	return t_idx


def check_hlist(val):
	h_idx = 0

	for h_val in target_hs:
		if (h_val <= val):
			continue
		
		if h_val not in qry_idxs:
			continue

		h_idx = check_a2list(h_val)
		print('h idx', h_idx)

		if (h_idx > 0):
			break

	return h_idx


def check_a2list(val):
	a2_idx = 0

	for a2_val in target_a2s:
		if (a2_val <= val):
			continue
		
		if a2_val not in qry_idxs:
			continue

		a2_idx = check_ilist(a2_val)
		print('a2 idx', a2_idx)

		if (a2_idx > 0):
			break

	return a2_idx


def check_ilist(val):
	i_idx = 0

	for i_val in target_is:
		if (i_val <= val):
			continue
		
		if i_val not in qry_idxs:
			continue
		else:
			i_idx = i_val
			break

	print('i idx', i_idx)
	return i_idx




test = "trhdqwartripadjdkatpdhdtahasdfiataihipsfgshafhtgthfaifspjfaret"

matrix =[[1,10],[4,13],[10,15],[4,33],[4,42],[15,45],[-8,10]]

result = pattern(test, matrix)

print(result)

