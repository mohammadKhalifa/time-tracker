def add_time(t1 , t2) :
    """ 
    This method adds two string variables in the form HH:MM
    
    """

    h1 , m1 = t1.split(':')
    h2 , m2 = t2.split(':')
    h3 = int(h1) + int(h2)  ; m3 = int(m1) + int(m2)
    if m3 > 59 :
        h3 += m3 // 60
        m3 = m3%60
       
    return str(h3) +":" + str(m3)

