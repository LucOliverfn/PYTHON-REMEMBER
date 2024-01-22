def fat(N):
    if N ==0:
        return(1)
    else:
        return(N*fat(N-1))
