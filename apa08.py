l=open("apa08input.txt","r").readlines()
cmd=l[0].strip()
g={m.split()[0]: [k.strip() for k in m.split("(")[1][:-2].split(",")] for m in l[2:]}
ps=[k for k in g.keys() if k[-1]=="A"]
seen = [[(p,0)] for p in ps]
finder = [{(p,0)} for p in ps]
done = [False for p in ps]
looplen = [0 for p in ps]
i=0
while not all(done):
  j=i%len(cmd)
  ps=[g[p][cmd[j]=="R"]for p in ps]
  for k in range(len(ps)):
    if not done[k]:
      done[k] = (ps[k],j) in finder[k]
      if done[k]:
        looplen[k] = i-seen[k].index((ps[k],j))
        print(k,looplen[k],i)
      seen[k].append((ps[k],j))
      finder[k].add((ps[k],j))
  i+=1
  if i % 1_000 == 0: print(i, done)
  if all(p[-1]=="Z"for p in ps):
    print(i)
    break

