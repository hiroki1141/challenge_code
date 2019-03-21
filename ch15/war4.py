from random import shuffle

#カード1枚に関する定義
class Card:
	#カードの数字
	card_nums = [
		"2","3","4","5","6","7","8","9","10","J","Q","K","A"
	]
	
	#カードのマーク
	card_marks = [
		"SPADES","HARTS","DIAMONDS","CLUBS"
	]

	#初期化：カード情報登録
	def __init__(self,n,m):
		"""カードの数字とマークは整数で指定します"""
		self.num  = self.card_nums[n]
		self.mark = self.card_marks[m]
	
	#">"
	def __gt__(self,enemy):
		if self.num > enemy.num:
			return True
		elif self.num == enemy.num:
			return self.mark > enemy.mark
		else:
			return False

	#"<"
	def __lt__(self,enemy):
		if self.num < enemy.num:
			return True
		elif self.num == enemy.num:
			return self.mark < enemy.mark
		else:
			return False

	#print時の表示文字定義
	def __repr__(self):
		w = "{} of {}".format(self.num,self.mark)
		return w

#カード52枚でデッキを定義
class Deck:
	#初期化
	def __init__(self):
		self.cards = []
		for i in range(13):
			for j in range(4):
				self.cards.append(Card(i,j))
		shuffle(self.cards)

	#デッキからカードを1枚ドロー
	def draw(self):
		if len(self.cards) == 0:
			return None
		else:
			return self.cards.pop()

#プレイヤーの定義
class Player:
	def __init__(self,name):
		self.name = name
		self.wins = 0
		self.card = None

#ゲーム本編の定義
class Game:
	#ゲーム初期化
	def __init__(self):
		name1 = input("プレイヤー１の名前：")
		name2 = input("プレイヤー２の名前：")
		self.game_deck = Deck()
		self.p1 = Player(name1)
		self.p2 = Player(name2)

	#ドローカードの表示
	def print_draw_cards(self,p1,p2):
		w = "{} は {} を、{} は {} を引きました"
		print(w.format(p1.name,p1.card,p2.name,p2.card))

	#ラウンド勝者の表示
	def print_round_winner(self,p):
		w = "このラウンドは {} の勝利"
		print(w.format(p.name))

	#これまでの戦績を表示
	def print_total_result_current(self,p):
		w = "{}：{}勝"
		print(w.format(p.name,p.wins))

	#ゲームフロー
	def play_game(self):
		#導入
		print("さぁ戦争を始めよう")
		print("-----")
		
		#本ループ
		while len(self.game_deck.cards) >= 2:
			#ゲーム継続意思の確認
			print("残カード枚数：{}枚".format(len(self.game_deck.cards)))
			game_quite = input("ゲームを終えるならq、続けるならq以外のキーを入力：")
			if game_quite == 'q':
				break
			
			#カードのドロー
			self.p1.card = self.game_deck.draw()
			self.p2.card = self.game_deck.draw()
			self.print_draw_cards(self.p1,self.p2)

			#勝敗判定
			if self.p1.card > self.p2.card:
				self.p1.wins += 1
				self.print_round_winner(self.p1)
			else:
				self.p2.wins += 1
				self.print_round_winner(self.p2)

			#
			self.print_total_result_current(self.p1)
			self.print_total_result_current(self.p2)
			print("-----")

		#最終勝敗判定
		if self.p1.wins > self.p2.wins:
			print("最終戦績：{}の勝ち - {}勝".format(self.p1.name,self.p1.wins))
		elif self.p1.wins < self.p2.wins:
			print("最終戦績：{}の勝ち - {}勝".format(self.p2.name,self.p2.wins))
		else:
			print("最終戦績：引き分け")

#戦争開始
game = Game()
game.play_game()