# LiuTaoTao github.com/Bookaa/LiuD

import re

def tostr_Python_STRING(s):
    if s is None:
        return None
    if (s[0],s[-1]) == ("'","'"):
        s = s[1:-1]
    return s
def tostr_Out_STRING(s):
    if s is None:
        return None
    if (s[0],s[-1]) == ("'","'"):
        s = s[1:-1]
    return s
def tostr_LiuD_STRING(s):
    if s is None:
        return None
    if (s[0],s[-1]) == ("'","'"):
        s = s[1:-1]
    return s
def tostr_LangL_STRING1(s):
    if s is None:
        return None
    if (s[0],s[-1]) == ('"','"'):
        s = s[1:-1]
    return s
def tostr_LangL_STRING2(s):
    if s and s[0] == '"':
        return s[1:]
    return s
def tostr_LangL_STRING3(s):
    return s
def tostr_LangL_STRING4(s):
    if s and s[-1] == '"':
        return s[:-1]
    return s
def tostr_Swift_STRING1(s):
    if s is None:
        return None
    if (s[0],s[-1]) == ('"','"'):
        s = s[1:-1]
    return s
def tostr_Swift_STRING2(s):
    if s and s[0] == '"':
        return s[1:]
    return s
def tostr_Swift_STRING3(s):
    return s
def tostr_Swift_STRING4(s):
    if s and s[-1] == '"':
        return s[:-1]
    return s

class HowRe:
    def __init__(self, s):
        self.compiled = re.compile(s, re.VERBOSE)
    def howmatch(self, textsrc, pos):
        m = self.compiled.match(textsrc, pos)
        if m:
            return (m.group(), m.end())
        return None

class IgnoreCls:
    def __init__(self, chars, strlst):
        self.ignore_chars = chars
        self.lex_ignores = [HowRe(s) for s in strlst]


class Parser00:
    def __init__(self, srctxt):
        self.srctxt = srctxt
        self.pos = [0, []]
        self.lastpos = 0
        self.skips = []
    def getpos(self):
        return (self.pos[0], self.pos[1]+[])
    def setpos(self, sav):
        self.pos[0] = sav[0]
        self.pos[1] = sav[1] + []
    def updatelast(self):
        if self.pos[0] > self.lastpos:
            self.lastpos = self.pos[0]
    def handle_OpChar(self, s):
        if self.pos[0] >= len(self.srctxt):
            return None
        i = 0
        for c in s:
            if self.pos[0]+i >= len(self.srctxt):
                return None
            c2 = self.srctxt[self.pos[0] + i]
            if c != c2:
                return None
            i += 1
        self.pos[0] += i; self.updatelast()
        return s
    def handle_anychar(self):
        if self.pos[0] >= len(self.srctxt):
            return None
        c = self.srctxt[self.pos[0]]
        self.pos[0] += 1
        return c
    def handle_Lex(self, lex, s = None):
        #b = match_compiled(lex, self.srctxt, self.pos[0])
        b = lex.howmatch(self.srctxt, self.pos[0])
        if b is not None:
            (value, m_end) = b
            if s is not None:
                if value != s:
                    return None
            self.pos[0] = m_end; self.updatelast()
            return value
        return None

    def Skip(self, n):
        self.SkipComments(self.skips[n])

    def SkipComments(self, syntax):
        if self.pos[0] >= len(self.srctxt):
            return
        ignore_chars = syntax.ignore_chars
        savpos = self.pos[0]
        while True:
            while self.pos[0] < len(self.srctxt):
                c = self.srctxt[self.pos[0]]
                if c in ignore_chars:
                    self.pos[0] += 1
                    continue
                break
            for lexed in syntax.lex_ignores:
                m = lexed.howmatch(self.srctxt, self.pos[0])
                if m:
                    self.pos[0] = m[1]; self.updatelast()
                    break
            if savpos == self.pos[0]:
                break

            self.updatelast()
            if self.pos[0] >= len(self.srctxt):
                return
            savpos = self.pos[0]

    def GetOpInLst(self, lst):
        for op in lst:
            s = self.handle_OpChar(op)
            if s is not None:
                return s
        return None

    def handle_ENDMARKER(self):
        if self.pos[0] == len(self.srctxt):
            return 'really end' # anything not None
        return None

    def GetLast(self):
        lst = self.srctxt[:self.lastpos].split('\n')
        lastline = lst[-1]
        lastlineno = len(lst)
        lastcolumn = len(lastline)
        return self.lastpos, lastlineno, lastcolumn, lastline
    def skipEmptyLine(self, ign):
        sav33 = self.pos[0]
        ignore1 = IgnoreCls(' \t', [])
        while True:
            self.SkipComments(ignore1)
            self.SkipComments(ign)
            if self.handle_OpChar('\n') is None:
                self.pos[0] = sav33
                return
            sav33 = self.pos[0]
    def handle_IdentAdd(self, ign):
        sav = self.pos[0]
        ignore_wspace = IgnoreCls(' \t', [])
        self.SkipComments(ignore_wspace)
        if self.pos[0] >= len(self.srctxt):
            self.pos[0] = sav
            return False
        c = self.srctxt[self.pos[0]]
        if c != '\n':
            self.pos[0] = sav
            return False
        self.pos[0] += 1
        self.skipEmptyLine(ign)
        s0 = ''
        identlst = self.pos[1]
        if identlst:
            last = identlst[-1]
            if self.handle_OpChar(last) is None:
                self.pos[0] = sav
                return False
            s0 = last
        s = self.Get_wspace()
        if s == '':
            self.pos[0] = sav
            return False
        identlst.append(s0 + s)
        return True
    def handle_IdentSub(self, ign):
        identlst = self.pos[1]
        if not identlst:
            return False
        sav = self.pos[0]
        ignore_wspace = IgnoreCls(' \t', [])
        self.SkipComments(ignore_wspace)
        if self.pos[0] >= len(self.srctxt):
            self.pos[0] = sav
            return False
        c = self.srctxt[self.pos[0]]
        if c != '\n':
            self.pos[0] = sav
            return False
        self.pos[0] += 1
        self.skipEmptyLine(ign)
        s = self.Get_wspace()
        self.pos[0] = sav   # yes
        if len(identlst) == 1:
            if s != '':
                return False
            identlst.pop()
            return True

        last2 = identlst[-2]

        if not last2.startswith(s):
            return False
        identlst.pop()
        return True
    def handle_IdentEqu(self, ign):
        sav = self.pos[0]
        ignore_wspace = IgnoreCls(' \t', [])
        self.SkipComments(ignore_wspace)
        if self.pos[0] >= len(self.srctxt):
            self.pos[0] = sav
            return False
        c = self.srctxt[self.pos[0]]
        if c != '\n':
            self.pos[0] = sav
            return False
        self.pos[0] += 1
        self.skipEmptyLine(ign)
        identlst = self.pos[1]
        if identlst:
            last = identlst[-1]
            if self.handle_OpChar(last) is None:
                self.pos[0] = sav
                return False
        s = self.Get_wspace()
        if s != '':
            self.pos[0] = sav
            return False
        return True
    def Get_wspace(self):
        s = ''
        while self.pos[0] < len(self.srctxt):
            c = self.srctxt[self.pos[0]]
            if c in ' \t':
                s += c
                self.pos[0] += 1
                continue
            break
        self.updatelast()
        return s
    def handle_Ident(self, s, ign):
        if s == '+ident':
            return self.handle_IdentAdd(ign)
        if s == '=ident':
            return self.handle_IdentEqu(ign)
        if s == '-ident':
            return self.handle_IdentSub(ign)
        assert False


class OutPrt:
    def __init__(self):
        self.lst = []
        self.identn = 0
        self.flink = False
    def identin(self):
        self.newline()
        self.identn += 1
    def identout(self):
        self.newline()
        self.identn -= 1
    def lnk(self):
        self.flink = True
    def puts(self, s):
        if isinstance(s, int):
            s = str(s)
        assert isinstance(s, str)
        if self.flink:
            self.flink = False
            if self.lst:
                self.lst[-1] += s
                return
        self.lst.append(s)
    def newline(self):
        if not self.lst:
            return
        s1 = '    ' * self.identn + ' '.join(self.lst)
        print s1
        self.lst = []

def PythonString(s):
    return str([s])[1:-1]

#lestr = r'".*?(?=\\\(|")"'
lestr = '".*?"'
lestr = r'"([^\\]|\\[^(])*?"'
lestr = r'".*?(?=\\\()'
s_sample = r'"I know a is \(a) \"and b is \(b) and c+b=\(c+b)d" dd'
s_sample = r'"I know a is \-(a) \"and b is \(b) and c+b=\-(c+b)d" dd'

if __name__ == '__main__':
    import Re2

    HowRe = Re2.HowRe_liud

    the = HowRe(lestr)
    print the.howmatch(s_sample, 0)