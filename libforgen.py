# LiuTaoTao github.com/Bookaa/LiuD

from Ast_LiuD import *

class OutP:
    def __init__(self, identn=0):
        self.s = ""
        self.identn = identn
        self.fDone = False
    def down(self):
        self.identn += 1
    def up(self):
        self.identn -= 1
    def prt(self, s):
        self.s += s
    def prtln(self, s, n = 0):
        s1 = '    '*(self.identn + n) + self.s + s
        print s1
        self.s = ""
        self.fDone = True

def PythonString(s):
    if len(s) > 60 and '\n' in s:
        if '\\' in s and not AnyEscapeChar(s):
            return "r'''%s'''" % s
        return "'''%s'''" % s
    return str([s])[1:-1]

def AnyEscapeChar(s):
    return False

def SwiftString(s):
    s0 = ''
    #savlast = ''
    for c in s:
        #if savlast != '':
        #    assert savlast == '\\'
        #    if c == '\\':
        #        s0 += r'\\'
        #    else:
        #        s0 += r'\\'+c
        #    savlast = ''
        #    continue
        if c == '\\':
            s0 += r'\\'
            #savlast = c
        elif c == '\t':
            s0 += r'\t'
        elif c == '"':
            s0 += r'\"'
        elif c == '\n':
            s0 += r'\n'
        else:
            s0 += c
    #if savlast != '':
    #    s0 += r'\\'
    #assert savlast == ''
    if s0 == r'\\\\':
        pass
    s2 = '"%s"' % s0
    #print 'SwiftString <%s> <%s>' % (s, s2)
    # <\#.*> <"\#.*">
    return s2
def SwiftStringMultiLine(s):
    lst = s.split('\n')
    lst2 = [SwiftString(a+'\n') for a in lst]
    s9 = ' +\n        '.join(lst2)
    return s9

def smarttype(s, SynName):
    if s.startswith('vlst'): return '[AST_%s]' % SynName
    if s.startswith('v'):
        if s.endswith('q'):
            return 'AST_%s?' % SynName
        return 'AST_%s' % SynName
    if s.startswith('slst'): return '[String]'
    if s.startswith('s'):
        if s.endswith('q'):
            return 'String?'
        return 'String'
    assert False, 'good' + s

class SmartType:
    def __init__(self, typ, typ2):
        self.typ = typ
        self.typ2 = typ2
    def howwalkmember(self,s):
        if self.typ2 in ('slst', 'nlst'):
            return 'self.outp.puts(%s)' % s
        return '%s.walkabout(self)' % s
    def howwalk(self,s):
        if Dest == 'swift':
            if self.typ2 in ('vq','sq','nq'): #.endswith('q'):
                s += '!'
        if self.typ2 in ('s','sq', 'n', 'nq', 'i', 'iq', 'f', 'fq', 'b'): #arg.startswith('s'):
            return 'self.outp.puts(%s)' % s
        return '%s.walkabout(self)' % s

def smartq(arg123):
    s, typ, typ2 = arg123
    if typ2 in ('v','s','i','f','n'):
        return s + '!'
    return s

def smarttyp2(s, typ2):
    if typ2 == 'vlstq': #s.endswith('*'):
        if s.endswith('?'): s = s[:-1]
        if s.endswith('*'): s = s[:-1]
        if s == '.v': return '[AST_%s]?' % SynName
        if s.startswith('.'): return '[%s_%s]?' % (s[1:], SynName)
        return '[%s_%s]?' % (SynName, s)
    if typ2 == 'vlst': #s.endswith('*'):
        if s.endswith('*'):
            s = s[:-1]
        if s == '.v':
            return '[AST_%s]' % SynName
        if s.startswith('.'):
            return '[%s_%s]' % (s[1:], SynName)
        return '[%s_%s]' % (SynName, s)
    if typ2 == 'v':
        if s == '.v':
            return 'AST_%s' % SynName
        if s.startswith('.'):
            return '%s_%s' % (s[1:], SynName)
        return '%s_%s' % (SynName, s)
    if typ2 == 'vq':
        if s == '.v?':
            return 'AST_%s?' % SynName
        if s.startswith('.'):
            if s[-1] == '?':
                return '%s_%s?' % (s[1:-1], SynName)
            return '%s_%s' % (s[1:], SynName)
        return '%s_%s' % (SynName, s)
    if typ2 == 'i': return 'Int'
    if typ2 == 'f': return 'Double'
    if typ2 == 'b': return 'Bool'
    if typ2 in ('s','n'): return 'String'
    if typ2 in ('sq','nq'): return 'String?'
    if typ2 in ('slst','nlst'): return '[String]'
    assert False


class Visit_00(LiuD_sample_visitor_01):
    def __init__(self, dic):
        self.dic = dic
    def visit_opt2(self, node):
        r = self.howword(node.s)

        return r + [('s','.s')] + r
    def visit_optgroup(self, node):
        r0 = None
        for v in node.vlst:
            result = v.walkabout(self)
            if result is None:
                continue
            assert len(result) == 1
            if r0 is None:
                r0 = result[0]
                continue
            assert False
        a,b = r0
        return [(a+'q', b+'?')]
    def visit_itemq(self, node):
        r0 = node.v.walkabout(self)
        if r0 is None:
            return None
        assert len(r0) == 1
        a,b = r0[0]
        return [(a+'q', b+'?')]
    def visit_choices(self, node):
        r0 = None
        for v in node.vlst :
            result = v.walkabout(self)
            assert result is not None
            assert len(result) == 1
            if r0 is None:
                r0 = result[0]
            else:
                a1,b1 = r0
                a2,b2 = result[0]
                if r0 == result[0]:
                    continue
                if a1 == a2 == 'v':
                    if b1 != b2:
                        s77 = self.combintype(b1,b2)
                        r0 = 'v',s77
                        continue
                    r0 = 'v', b1
                    continue
                if a1 == a2 == 's':
                    r0 = 's', '.s'
                    continue
                print 'error choice', a1, a2
                assert False
        return [r0]
    def combintype(self,b1,b2):
        if b1.startswith('.'):
            s1 = b1
        elif b1 in self.dic:
            the1 = self.dic[b1]
            s1 = '.' + the1.protcl
        else:
            return '.v'

        if b2.startswith('.'):
            s2 = b2
        elif b2 in self.dic:
            the2 = self.dic[b2]
            s2 = '.' + the2.protcl
        else:
            return '.v'
        if s1 == s2:
            return s1
        return '.v'
    def visit_serie(self, node):
        a1 = []
        for v in node.vlst:
            result = v.walkabout(self)
            if result is not None:
                a1.extend(result)
        if a1:
            return a1
        return None
    def visit_jiad(self, node):
        r1 = node.v1.walkabout(self)
        assert len(r1) == 1
        r2 = node.v4.walkabout(self)
        if r2 is None:
            return [(r1[0][0] + 'lst', r1[0][1] + '*')]
        assert False
    def visit_jiap(self, node):
        r1 = node.v1.walkabout(self)
        assert len(r1) == 1
        r2 = node.v4.walkabout(self)
        if r2 is None:
            return [(r1[0][0] + 'lst', r1[0][1] + '*')]
        assert len(r2) == 1
        return [(r1[0][0] + 'lst', r1[0][1] + '*'), (r2[0][0] + 'lst', r2[0][1] + '*')]
    def visit_itemd(self, node):
        result = node.v.walkabout(self)
        if result is None:
            return None
        assert len(result) == 1, len(result)
        return [(result[0][0] + 'lst', result[0][1] + '*')]
    def visit_itemp(self, node):
        result = node.v.walkabout(self)
        if result is None:
            return None
        assert len(result) == 1
        return [(result[0][0] + 'lst', result[0][1] + '*')]
    def visit_LitName(self, node):
        return self.howword(node.n)
    def howword(self, s):
        if s in base_def:
            typdefs, _ = base_def[s]
            if typdefs in ('String','String2'):
                return [('s','.s')]
            if typdefs == 'Int':
                return [('i','.i')]
            if typdefs == 'Double':
                return [('f','.f')]
            if typdefs == 'Name':
                return [('n','.n')]
            assert False
        if s in self.dic:
            if s == 'value05':
                pass
            node1 = self.dic[s].node
            if isinstance(node1, LiuD_stmt_inline):
                if node1.s == 'dotsth':
                    pass
                result = node1.v.walkabout(self)
                if result is None:
                    return None
                return result
            elif isinstance(node1, LiuD_stmt_tax):
                if isinstance(node1.v, LiuD_opt2):
                    s = node1.v.s
                    return self.howword(s)
                if isinstance(node1.v, LiuD_MoreDef):
                    s_prot = self.dic[s].protcl
                    return [('v', '.%s' % s_prot)]
                return [('v', s)]
            else:
                assert False
    def visit_bracechoice(self, node):
        r0 = None
        for v in node.vlst :
            result = v.walkabout(self)
            if result is None:
                pass
            assert result is not None
            assert len(result) == 1
            if r0 is None:
                r0 = result[0]
            else:
                a1,b1 = r0
                a2,b2 = result[0]
                if (a1,a2) == ('n','s'):
                    r0 = 'n', '.n'
                    continue
                if a1 == a2 == 'v':
                    if b1 != b2:
                        r0 = 'v',self.combintype(b1,b2)
                        continue
                    r0 = 'v', b1
                    continue
                if a1 == a2 == 's':
                    if b1 != b2:
                        r0 = 's', '.s'
                        continue
                    r0 = 's', b1
                    continue
                assert False
        return [r0]
    def visit_BoolChoice(self, node):
        return [('b','.b')]
    def visit_BoolIf(self, node):
        return [('b','.b')]
    def visit_basestrn(self, node):
        if isinstance(node.v, LiuD_LitName):
            pass # do nothing
        else:
            return [('s','.s')]
    def visit_inline(self, node):
        return [('v', node.v.s)]
    def visit_OtherSyntax(self, node):
        return [('s','.s'),('s','.s'),('v','.v')]
    def visit_MoreDef(self, node):
        a1 = []
        for v in node.vlst:
            result = v.walkabout(self)
            if result is not None:
                a1.extend(result)
        if a1:
            return a1
        return None

class LiudNodeInfo:
    def __init__(self, node, syntax, protcl, linecmt):
        self.node = node
        self.ign_syntax = syntax
        self.protcl = protcl
        self.linecmt = linecmt

class Visit_Gen01(LiuD_sample_visitor_01):
    def __init__(self):
        self.cur_syntax = '-'
        self.lst0 = [] # only save name, for keep sequence
        self.dic = {}
        self.cur_protocol = 'AST' #_%s' % SynName
        self.linecomment = ''
    def visit_protoGroup(self, node):
        sav = self.cur_protocol
        self.cur_protocol = node.n
        for v in node.vlst:
            v.walkabout(self)
        self.cur_protocol = sav
    def visit_dot_syntax(self, node):
        self.cur_syntax = node.n
    def visit_set_linecomment(self, node):
        self.linecomment = node.s
    def visit_stmt_tax(self, node):
        self.lst0.append(node.s)
        self.dic[node.s] = LiudNodeInfo(node, self.cur_syntax, self.cur_protocol, self.linecomment)

        node.v.walkabout(self)
    def visit_stmt_inline(self, node):
        self.lst0.append(node.s)
        self.dic[node.s] = LiudNodeInfo(node, self.cur_syntax, self.cur_protocol, self.linecomment)

        node.v.walkabout(self)
    def AllLst(self):
        for name in self.lst0:
            if name == 'enumdef':
                pass
            nodeinfo = self.dic[name]
            node = nodeinfo.node
            if isinstance(node, LiuD_stmt_inline):
                if node.vargq is not None:
                    arglst = [node.vargq.s]
                    _, arglst2, arglst3 = self.TryGetArgLst(node.v, arglst)
                else:
                    arglst, arglst2, arglst3 = self.TryGetArgLst(node.v, [])
                    assert len(arglst) == 1
            elif isinstance(node, LiuD_stmt_tax):
                if node.vq is not None:
                    arglst = []
                    for a in node.vq.vlst:
                       arglst.append(a.s)
                    _, arglst2, arglst3 = self.TryGetArgLst(node.v, arglst)
                else:
                    arglst, arglst2, arglst3 = self.TryGetArgLst(node.v, [])
            else:
                assert False
            nodeinfo.arglst = zip(arglst, arglst2, arglst3)
        return GrammarList(self.lst0, self.dic)
    def TryGetArgLst(self, node, lst0):
        visit = Visit_00(self.dic)
        lst3 = node.walkabout(visit)
        if lst3 is None:
            return [],[],[]

        arglst = []; typlst = []
        for a,b in lst3:
            arglst.append(a)
            typlst.append(b)

        if lst0:
            assureArgName(lst0, arglst)
            return NoSameName(lst0), typlst, arglst
        return NoSameName(arglst), typlst, arglst

def NoSameName(lst):
    lst2 = []
    for i,s in enumerate(lst):
        if CountN(lst,s) > 1:
            lst2.append('%s%d' % (s, i+1))
        else:
            lst2.append(s)
    return lst2
def CountN(lst, v):
    n = 0
    for s in lst:
        if s == v:
            n+=1
    return n

def assureArgName(lst1,lst2):
    if len(lst1) != len(lst2):
        pass
    assert len(lst1) == len(lst2)
    for i in range(len(lst1)):
        continue
        s1 = lst1[i]
        s2 = lst2[i]
        if s1.startswith('vlst') or s2.startswith('vlst'):
            assert s1.startswith('vlst')
            assert s2.startswith('vlst')
        if s1.startswith('slst') or s2.startswith('slst'):
            assert s1.startswith('slst')
            assert s2.startswith('slst')
        if s1.startswith('v') or s2.startswith('v'):
            assert s1.startswith('v')
            assert s2.startswith('v')
        if s1.startswith('s') or s2.startswith('s'):
            assert s1.startswith('s')
            assert s2.startswith('s')
        if s1.endswith('q') or s2.endswith('q'):
            assert s1.endswith('q')
            if not s2.endswith('q'):
                pass
            assert s2.endswith('q')

class GrammarList:
    def __init__(self, lst, dic):
        self.lst = lst
        self.dic = dic

    def iter_all(self):
        for name in self.lst:
            nodeinfo = self.dic[name]
            yield nodeinfo

    def iter_syntax(self):
        for name in self.lst:
            nodeinfo = self.dic[name]
            if isinstance(nodeinfo.node, LiuD_stmt_tax):
                yield nodeinfo

    def ifinline(self, name):
        if name not in self.dic:
            return False
        nodeinfo = self.dic[name]
        return isinstance(nodeinfo.node, LiuD_stmt_inline)

    def handle_LitName(self, node):
        if not isinstance(node, LiuD_LitName):
            pass
        assert isinstance(node, LiuD_LitName)
        if self.ifinline(node.n):
            return 'self.hdl_%s()' % node.n
        return 'self.handle_%s()' % node.n
