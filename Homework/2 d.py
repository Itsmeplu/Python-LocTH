bronze_chest = int(input())
silver_chest = int(input())
gold_chest = int(input())

if bronze_chest + silver_chest >= bronze_chest + gold_chest and bronze_chest + silver_chest >= silver_chest + gold_chest :
    result = bronze_chest + silver_chest
elif bronze_chest + gold_chest >= bronze_chest + silver_chest and bronze_chest + gold_chest >= silver_chest + gold_chest :
    result = bronze_chest + gold_chest
elif silver_chest + gold_chest >= bronze_chest + gold_chest and silver_chest + gold_chest >= bronze_chest + silver_chest :
    result = silver_chest + gold_chest

print(result)