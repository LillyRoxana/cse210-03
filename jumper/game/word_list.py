try:

  import random
  class word_list:
    def __init__(self):
      word_list = {
      1: "wares",
      2: "soup",
      3: "mount",
      4: "extend",
      5: "brown",
      6: "expert",
      7: "tired",
      8: "humidity",
      9: "backpack",
      10: "crust",
      11: "dent",
      12: "market",
      13: "knock",
      14: "smite",
      15: "windy",
      16: "coin",
      17: "silence",
      18: "bluff",
      19: "climb",
      20: "ying",
      21: "weaver",
      22: "snob",
      23: "kickoff",
      24: "match",
      25: "quaker",
      26: "foreman",
      27: "excite",
      28: "thinking",
      29: "mend",
      30: "allergen",
      31: "pruning",
      32: "coat",
      33: "emerald",
      34: "coherent",
      35: "manic",
      36: "multiple",
      37: "square",
      38: "funded",
      39: "funnel",
      40: "sailing",
      41: "dream",
      42: "mutation",
      43: "strict",
      44: "mystic",
      45: "film",
      46: "guide",
      47: "strain",
      48: "bishop",
      49: "settle",
      50: "plateau",
      51: "emigrate",
      52: "marching",
      53: "optimal",
      54: "medley",
      55: "endanger",
      56: "wick",
      57: "condone",
      58: "schema",
      59: "rage",
      60: "figure",
      61: "plague",
      62: "aloof",
      63: "there",
      64: "reusable",
      65: "refinery",
      66: "suffer",
      67: "affirm",
      68: "captive",
      69: "flipping",
      70: "prolong",
      71: "main",
      72: "coral",
      73: "dinner",
      74: "rabbit",
      75: "chill",
      76: "seed",
      77: "born",
      78: "shampoo",
      79: "italian",
      80: "giggle",
      81: "roost",
      82: "palm",
      83: "globe",
      84: "wise",
      85: "grandson",
      86: "running",
      87: "sunlight",
      88: "spending",
      89: "crunch",
      90: "tangle",
      91: "forego",
      92: "tailor",
      93: "divinity",
      94: "probe",
      95: "bearded",
      96: "premium",
      97: "featured",
      98: "serve",
      99: "borrower",
      100: "examine",
      
     }
      choose = random.randint(1,100)
      self._word_list = word_list[choose].lower()

      def letter_found(self, guessed_word):
        for letter in self._word_list:
          if letter in guessed_word:
            pass
          else:
            return True
        return False 
  

      def compare(self, guess_player):
        guess = ""
        for letter in self._word_list:
          if letter in guess_player._word_list:
            guess += letter
          else:
              guess += "_"
        return guess

      def lets_to_count_attempts(self, guess_player):
        attempt = 0
        for guess_letter in guess_player._word_list:
          if guess_letter in self._word_list:
            pass
          else:
            attempt += 1
        return attempt    



except ModuleNotFoundError:
    print('\nError [random] can´t be located by word_list.py...') 
