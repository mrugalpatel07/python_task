data=[
{"item":"apple","qty":10,"price":0.5},
{"item":"banana","qty":5,"price":0.3},
{"item":"orange","qty":8,"price":0.6},
{"item":"apple","qty":7,"price":0.5},
{"item":"banana","qty":3,"price":0.3},
{"item":"orange","qty":6,"price":0.6}
]

report={}

for i in data:
 name=i["item"]
 qty=i["qty"]
 rate=i["price"]
 money=qty*rate
 if name not in report:
  report[name]={}
  report[name]["total_qty"]=0
  report[name]["total_money"]=0
 report[name]["total_qty"]=report[name]["total_qty"]+qty
 report[name]["total_money"]=report[name]["total_money"]+money

print("total quantity:")
for x in report:
 print(x,"=",report[x]["total_qty"])
print("total money:")
for x in report:print(x,"=",report[x]["total_money"])

max_qty=0
max_name=""
for x in report:
 if report[x]["total_qty"]>max_qty:
  max_qty=report[x]["total_qty"]
  max_name=x
print("most sold item:",max_name,"with",max_qty)

max_money=0
top_name=""
for x in report:
 if report[x]["total_money"]>max_money:
  max_money=report[x]["total_money"]
  top_name=x
print("highest money item:",top_name,"with",max_money,"rs")
