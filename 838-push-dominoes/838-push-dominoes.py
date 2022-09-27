class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pushed = ''
        while pushed != dominoes:
            pushed = dominoes
            dominoes = dominoes.replace('R.L', '000')
            dominoes = dominoes.replace('.L', 'LL')
            dominoes = dominoes.replace('R.', 'RR')
        dominoes = dominoes.replace('000', 'R.L')
        return dominoes
            