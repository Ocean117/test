# -*- coding:utf-8 -*-

print("\n".join(["\t".join(["%s*%s=%s" %(x,y,x*y) for y in range(1,x+1)) for x in range(1,10)]))
