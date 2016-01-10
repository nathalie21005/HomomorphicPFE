the steps of EuclideanDistanceEncrypted.py:

in def encrypt_euclidean_distance:
    i get w , w_2 , cw_2, and dw_2 then verify w_2=dw_2
	i get v , cv, dv , v_2, cv_2, dv_2 the i verify v=dv and v_2=dv_2
	i add : add=cv_2 and cw_2 
	i multiply: multi= (-2)*w then multiply by cv multi= (2_w*cv) and check if the value is negative , do %pub.n else no
	then i add: add and multi by call the function e_add
	then i have the encrypted distance positve but the decryption of the distance !!!!!!!