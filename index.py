# 1st input: enter height in meters e.g:1.65
height =(input("Boy: "))
# 2st input: weight in kilograms e.g:75
weight =(input("Kilo: "))
height_as_int=float(height)
weight_as_int=int(weight)

bmi=weight_as_int / height_as_int**2

bmi_as_int=int(bmi)

print(f"Vucut kitle endeksiniz {bmi_as_int}")


if(bmi < 18.5) : 
    print("İdeal kilonun altında")
elif(bmi>=18.5 and bmi<=24.9):
    print("İdeal kiloda")
elif(bmi>=25 and bmi<=29.9):
    print("İdeal klüonun üstünde")
elif(bmi>=30 and bmi<=39.9):
    print("İdeal kilonun çok üstünde (obez)")
else :
    print("İdeal kilonun çok üstünde (morbid obez)")