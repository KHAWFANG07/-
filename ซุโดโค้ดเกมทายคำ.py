#pseudo-code

#ตัวแปรที่ระบุสถานะของเกม
score = 0
lives = 3
words = [ 'fang' , 'oat','tran']

#ตราบใดที่มีคำให้ทายอยู่ และ ชีวิตยังเหลือ --> เล่นต่อไป
while (ยังมีคำให้ทาย) and (ชีวิตยังเหลือ):
    #สุ่มคำจาก words แล้วดึงคำนั้นออกจาก list
    secret_word = คำที่สุ่ม
    clue = ['?','?'....]จำนวนเท่ากับตัวอักษรของ secret_word
    #ตราบใดที่ยังทายคำนี้ไม่เสร็จหรือชีวิตยังไม่หมด
    while ยังทายไม่เสร็จ:
        print(clue)
        print('ชีวิตที่เหลือ:'+lives)
        guess = input('ทายอักษรมาซิ: ')
        #chek ว่าตัวอักษรที่ทายอยู่ใน secret_word ป่าว
        if guess in secret_word:
            win = update_clue(guess,secret_word,cule)
            if win:
                print('เย้! คำนั้นก็คือ:  '+secret_word)
                print('socre: ' +score)
        else: #ที่ guss มา ไม่อยู่ใน secret_word
            print('ผิด! เลือดลด')
            lives = lives-1
            if lives == 0:
                print('แแพ้แล้ว คำนั้นคือ: ' + secret_word)
                break

print('final score:'+socre)
print('Game end!')
