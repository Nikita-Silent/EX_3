# Developer Drachev N.
import local as lc
import math as m

print(lc.INTRO)
veight, kg = map(int, input().split())
while lc.kal_swim < (kg * 7716):
    lc.x += 1
    lc.kal_swim += 7 * veight
while lc.kal_run < (kg * 7716):
    lc.y += 1
    lc.kal_run += 2 * veight

print(lc.BEST_TIME, m.ceil(lc.x/4), 'дней плавинием или в течение', m.ceil(lc.y/4), 'дней бегом.')
print(lc.FOOD)
food = int(input(lc.FOOD_2))

while lc.z < m.ceil(lc.x/4):
    lc.z += 1
    lc.food_2 += food
while lc.d < m.ceil(lc.y/4):
    lc.d += 1
    lc.food_3 += food
while lc.kal_swim_2 < (lc.food_2 * 4):
    lc.a += 1
    lc.kal_swim_2 += 7 * veight
while lc.kal_run_2 < (lc.food_3 * 4):
    lc.b += 1
    lc.kal_run_2 += 2 * veight

print(lc.FINAL, m.ceil(lc.a/4), 'дней плаванья или', m.ceil(lc.b/4), 'дней бега.')
print(lc.FINAL_SWIM, m.ceil(lc.a/4) + m.ceil(lc.x/4), ' дней;', '\n',
      lc.FINAL_RUN, m.ceil(lc.b/4) + m.ceil(lc.y/4), ' дней.', sep='')
print(lc.ADD)
for i in lc.WEEK_DAY:
    print(i, 'с 8:00 до 10:00 и с 18:00 до 20:00')