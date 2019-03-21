import random

def hangman():
	#変数:出題単語リスト系
	ans_words_list = [
		"java",
		"cat",
		"me"
	]
	ans_index = random.randint(0,len(ans_words_list)-1)
	ans_words = ans_words_list[ans_index]

	#変数:ステージ
	stage = [
		"-------------     ",
		"|       |         ",
		"|       |         ",
		"|       O         ",
		"|      /|\\       ",
		"|      / \\       ",
		"|                 ",
	]

	#変数:ゲーム制御系
	win = False
	wrong = 0
	print_words = ["-"] * len(ans_words)
	judge_words = list(ans_words)

	#本編:ゲーム開始
	print("ハングマンを始めます!")
	while wrong < len(stage)-1 :
		#入力受付
		print("\n")
		print(" ".join(print_words))
		ans_char = input("１文字入力してください：")
		
		#判定		
		if ans_char in judge_words:
			tmp_index = judge_words.index(ans_char)
			print_words[tmp_index] = ans_char
			judge_words[tmp_index] = "$"
		else:
			wrong += 1

		#勝利判定
		print("\n".join(stage[0:wrong+1]))
		if "-" not in print_words:
			win = True
			print("あなたの勝ちです")		
			print("正解の単語は{}です".format(ans_words))
			break

	#敗戦判定	
	if not win:
			print("あなたの負けです")		
			print("正解の単語は{}です".format(ans_words))		

hangman()