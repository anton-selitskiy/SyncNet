import os

r = ['b345b194da517c77.mp4',
 '664ffc49d4ed57c3.mp4',
 '860cc4c1fd2572cb.mp4',
 '7725e589a2895561.mp4',
 '00055cac1309f452.mp4',
 '61f11b2ce6b1302f.mp4',
 '47b3da77499cbb41.mp4',
 '5dba00b4f36a7ac4.mp4',
 '4fba22f7b3dfb87a.mp4',
 '2f15f0633e71d072.mp4',
 '29f6d2611b50c2e1.mp4',
 '88a72f780fbd4c5d.mp4',
 'f71c67334e90920f.mp4',
 '984c5c2711f2f8c6.mp4',
 '353ea08e6f2dbad1.mp4',
 '568299a1922713f1.mp4',
 '36d897133f774d15.mp4',
 '751dc59c35c1809d.mp4',
 'e94d3bb9ba11eb29.mp4',
 '17d688724cc4b6a4.mp4',
 '5fa4d9b3dc9e3493.mp4',
 '6d34f1732eefd576.mp4',
 '94763c88f22a1ace.mp4',
 'cb1346c67f6ee3aa.mp4',
 'c1b7b78abefc5f1b.mp4',
 '1fcf3ab3bdbc6fe3.mp4',
 '021bd9fbddb5a69c.mp4',
 '83c9b9aa2f9f38d3.mp4',
 '757030b1e70b0cf8.mp4',
 '8e51f9e10e471f53.mp4']

f = ['9a22372d22a52397.mp4',
 '9bc4f1306bb8e2cd.mp4',
 '88fe2a902a9d8cc7.mp4',
 '1f3cbda142d0944a.mp4',
 '63bed62257daccaf.mp4',
 'ee8e8d4a59a95d5f.mp4',
 '04011d0f6efa6d85.mp4',
 'cbcf9320b4e4d9f9.mp4',
 '262a25215787616d.mp4',
 'fbca2df503111454.mp4',
 '9149e78016d11aeb.mp4',
 'eacc6b7d3bdb8b39.mp4',
 '026646a4eb385e50.mp4',
 '8d2db652940a8dc8.mp4',
 'baf6dcb6e2196efa.mp4',
 '2c33dc22e961f0d7.mp4',
 'e4ed78bc2aa92b40.mp4',
 '77fb2d049f234fbd.mp4',
 '5fb85b52c7d4d045.mp4',
 'c0ed568e0489acd1.mp4',
 '1ddf59260ed2749f.mp4',
 'f1bcde07aba6649e.mp4',
 '975ff2ad09647e57.mp4',
 'bfe0f53abccde244.mp4',
 '386b9e08d7f2baf4.mp4',
 '3b045995aee69601.mp4',
 '3b02486d824f470b.mp4',
 '89fb00a09c49b44c.mp4',
 '88fe233425f6e6b6.mp4',
 'f1915a98a84d154b.mp4']

path = '/home/cxu-serve/p1/lchen63/trustyAI/videos/'
pathr = '/u/aselitsk/syncnet_python/output/r/'
pathf = '/u/aselitsk/syncnet_python/output/f/'

for file in r:
    path1 = path+file
    path2 = pathr+file
    os.system('cp '+path1+' '+ path2)
for file in f:
    path1 = path+file
    path2 = pathf+file
    os.system('cp '+path1+' '+path2)
