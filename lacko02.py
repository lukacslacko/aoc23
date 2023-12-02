#!/usr/bin/python3

def part1(lines):
  r=0
  for line in lines:
    l=line.split(':')
    lineid=int(l[0][5:])
    l=l[1].split(';')
    ip=True
    for q in l:
      for c in q.split(','):
        c=c.split(' ')
        if c[2]=='red' and int(c[1])>12:
          ip=False
        if c[2]=='green' and int(c[1])>13:
          ip=False
        if c[2]=='blue' and int(c[1])>14:
          ip=False
    if ip:
      r+=lineid
  return r

def part2(lines):
  r=0
  for line in lines:
    l=line.split(':')
    l=l[1].split(';')
    mr=0
    mg=0
    mb=0
    for q in l:
      for c in q.split(','):
        c=c.split(' ')
        if c[2]=='red':
          mr=max(mr,int(c[1]))
        if c[2]=='green':
          mg=max(mg,int(c[1]))
        if c[2]=='blue':
          mb=max(mb,int(c[1]))
    r+=mr*mg*mb
  return r

with open('lacko02input.txt', 'r') as f:
  lines = list(map(lambda l: l.strip(), f.readlines()))
  print('part1:', part1(lines))
  print('part2:', part2(lines))
