
import requests
from lxml import etree

url = "/mirror/scratch/ywang/NGC0253_Nakanishi/Tar/2016.1.00481.S/science_goal.uid___A001_X87c_X367/group.uid___A001_X87c_X368/member.uid___A001_X87c_X369/qa/pipeline-20171012T085955/html/stage19/t2-4m_details.html"


r = open(url,'r',encoding='utf-8')
r=r.read()

tree0bj = etree.HTML(r)
target = tree0bj.xpath("//table[@class='table table-striped']/tbody/tr/td/text()")

len(target)
print(target[0])
