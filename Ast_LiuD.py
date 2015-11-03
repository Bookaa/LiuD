# auto generate code, LiuTaoTao

from lib import *

class liud_opt2:
    def __init__(self, s, vlst):
        self.s = s
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_opt2(self)


class liud_choices:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_choices(self)


class liud_OtherSyntax:

    def walkabout(self, visitor):
        return visitor.visit_OtherSyntax(self)


class liud_stringchoice:
    def __init__(self, slst):
        self.slst = slst

    def walkabout(self, visitor):
        return visitor.visit_stringchoice(self)


class liud_inline:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_inline(self)


class liud_serie:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_serie(self)


class liud_bracegroup:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_bracegroup(self)


class liud_bracechoice:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_bracechoice(self)


class liud_ident:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_ident(self)


class liud_basestrn:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_basestrn(self)


class liud_ifnext:
    def __init__(self, slst):
        self.slst = slst

    def walkabout(self, visitor):
        return visitor.visit_ifnext(self)


class liud_ifnotnext:
    def __init__(self, slst):
        self.slst = slst

    def walkabout(self, visitor):
        return visitor.visit_ifnotnext(self)


class liud_itemq:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_itemq(self)


class liud_itemd:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_itemd(self)


class liud_itemp:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_itemp(self)


class liud_jiad:
    def __init__(self, v1, v2q, v3q, v4):
        self.v1 = v1
        self.v2q = v2q
        self.v3q = v3q
        self.v4 = v4

    def walkabout(self, visitor):
        return visitor.visit_jiad(self)


class liud_jiap:
    def __init__(self, v1, v2q, v3q, v4):
        self.v1 = v1
        self.v2q = v2q
        self.v3q = v3q
        self.v4 = v4

    def walkabout(self, visitor):
        return visitor.visit_jiap(self)


class liud_optgroup:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_optgroup(self)


class liud_syntaxdef:
    def __init__(self, n):
        self.n = n

    def walkabout(self, visitor):
        return visitor.visit_syntaxdef(self)


class liud_LitName:
    def __init__(self, n):
        self.n = n

    def walkabout(self, visitor):
        return visitor.visit_LitName(self)


class liud_LitString:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_LitString(self)


class liud_dot_syntax:
    def __init__(self, n):
        self.n = n

    def walkabout(self, visitor):
        return visitor.visit_dot_syntax(self)


class liud_stmt_inline:
    def __init__(self, s, vargq, v):
        self.s = s
        self.vargq = vargq
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_stmt_inline(self)


class liud_stmt_tax:
    def __init__(self, s, vq, v):
        self.s = s
        self.vq = vq
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_stmt_tax(self)


class liud_args:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_args(self)


class liud_arg:
    def __init__(self, s, sq):
        self.s = s
        self.sq = sq

    def walkabout(self, visitor):
        return visitor.visit_arg(self)


class liud_protoGroup:
    def __init__(self, n, vlst):
        self.n = n
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_protoGroup(self)


class liud_Module:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_Module(self)

class liud_sample_visitor_00:
    def visit_opt2(self, node): pass
    def visit_choices(self, node): pass
    def visit_OtherSyntax(self, node): pass
    def visit_stringchoice(self, node): pass
    def visit_inline(self, node): pass
    def visit_serie(self, node): pass
    def visit_bracegroup(self, node): pass
    def visit_bracechoice(self, node): pass
    def visit_ident(self, node): pass
    def visit_basestrn(self, node): pass
    def visit_ifnext(self, node): pass
    def visit_ifnotnext(self, node): pass
    def visit_itemq(self, node): pass
    def visit_itemd(self, node): pass
    def visit_itemp(self, node): pass
    def visit_jiad(self, node): pass
    def visit_jiap(self, node): pass
    def visit_optgroup(self, node): pass
    def visit_syntaxdef(self, node): pass
    def visit_LitName(self, node): pass
    def visit_LitString(self, node): pass
    def visit_dot_syntax(self, node): pass
    def visit_stmt_inline(self, node): pass
    def visit_stmt_tax(self, node): pass
    def visit_args(self, node): pass
    def visit_arg(self, node): pass
    def visit_protoGroup(self, node): pass
    def visit_Module(self, node): pass

class liud_sample_visitor_01:
    def visit_opt2(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_choices(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_OtherSyntax(self, node):
        pass
    def visit_stringchoice(self, node):
        pass
    def visit_inline(self, node):
        node.v.walkabout(self)
    def visit_serie(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_bracegroup(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_bracechoice(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_ident(self, node):
        pass
    def visit_basestrn(self, node):
        node.v.walkabout(self)
    def visit_ifnext(self, node):
        pass
    def visit_ifnotnext(self, node):
        pass
    def visit_itemq(self, node):
        node.v.walkabout(self)
    def visit_itemd(self, node):
        node.v.walkabout(self)
    def visit_itemp(self, node):
        node.v.walkabout(self)
    def visit_jiad(self, node):
        node.v1.walkabout(self)
        if node.v2q is not None:
            node.v2q.walkabout(self)
        if node.v3q is not None:
            node.v3q.walkabout(self)
        node.v4.walkabout(self)
    def visit_jiap(self, node):
        node.v1.walkabout(self)
        if node.v2q is not None:
            node.v2q.walkabout(self)
        if node.v3q is not None:
            node.v3q.walkabout(self)
        node.v4.walkabout(self)
    def visit_optgroup(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_syntaxdef(self, node):
        pass
    def visit_LitName(self, node):
        pass
    def visit_LitString(self, node):
        pass
    def visit_dot_syntax(self, node):
        pass
    def visit_stmt_inline(self, node):
        if node.vargq is not None:
            node.vargq.walkabout(self)
        node.v.walkabout(self)
    def visit_stmt_tax(self, node):
        if node.vq is not None:
            node.vq.walkabout(self)
        node.v.walkabout(self)
    def visit_args(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_arg(self, node):
        pass
    def visit_protoGroup(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_Module(self, node):
        for v in node.vlst:
            v.walkabout(self)

class liud_out_visitor_01:
    def __init__(self, outp):
        self.outp = outp
    def visit_opt2(self, node):
        self.outp.puts(node.s)
        self.outp.puts('^-')
        self.outp.puts('(')
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.puts(')')
    def visit_choices(self, node):
        tem1 = 0
        for tem2 in node.vlst:
            if tem1 > 0:
                self.outp.puts('\n    |')
            tem1 = 1
            tem2.walkabout(self)
    def visit_OtherSyntax(self, node):
        self.outp.puts('$NewSyntax')
    def visit_stringchoice(self, node):
        self.outp.puts('(')
        tem1 = 0
        for tem2 in node.slst:
            if tem1 > 0:
                self.outp.puts('|')
            tem1 = 1
            self.outp.puts(tem2)
        self.outp.puts(')')
    def visit_inline(self, node):
        self.outp.puts('(')
        node.v.walkabout(self)
        self.outp.puts(')')
    def visit_serie(self, node):
        for tem1 in node.vlst:
            tem1.walkabout(self)
    def visit_bracegroup(self, node):
        self.outp.puts('(')
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.puts(')')
    def visit_bracechoice(self, node):
        self.outp.puts('(')
        tem1 = 0
        for tem2 in node.vlst:
            if tem1 > 0:
                self.outp.puts('|')
            tem1 = 1
            tem2.walkabout(self)
        self.outp.puts(')')
    def visit_ident(self, node):
        self.outp.puts(node.s)
    def visit_basestrn(self, node):
        node.v.walkabout(self)
        self.outp.lnk()
        self.outp.puts('$')
    def visit_ifnext(self, node):
        self.outp.puts('-ifnext(')
        tem1 = 0
        for tem2 in node.slst:
            if tem1 > 0:
                self.outp.puts('|')
            tem1 = 1
            self.outp.puts(tem2)
        self.outp.puts(')')
    def visit_ifnotnext(self, node):
        self.outp.puts('-ifnotnext(')
        tem1 = 0
        for tem2 in node.slst:
            if tem1 > 0:
                self.outp.puts('|')
            tem1 = 1
            self.outp.puts(tem2)
        self.outp.puts(')')
    def visit_itemq(self, node):
        node.v.walkabout(self)
        self.outp.lnk()
        self.outp.puts('?')
    def visit_itemd(self, node):
        node.v.walkabout(self)
        self.outp.lnk()
        self.outp.puts('*')
    def visit_itemp(self, node):
        node.v.walkabout(self)
        self.outp.lnk()
        self.outp.puts('+')
    def visit_jiad(self, node):
        node.v1.walkabout(self)
        if node.v2q is not None:
            node.v2q.walkabout(self)
        self.outp.puts('^*')
        if node.v3q is not None:
            node.v3q.walkabout(self)
        node.v4.walkabout(self)
    def visit_jiap(self, node):
        node.v1.walkabout(self)
        if node.v2q is not None:
            node.v2q.walkabout(self)
        self.outp.puts('^+')
        if node.v3q is not None:
            node.v3q.walkabout(self)
        node.v4.walkabout(self)
    def visit_optgroup(self, node):
        self.outp.puts('[')
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.puts(']')
    def visit_syntaxdef(self, node):
        self.outp.puts('-(')
        self.outp.lnk()
        self.outp.puts(node.n)
        self.outp.lnk()
        self.outp.puts(')')
    def visit_LitName(self, node):
        self.outp.puts(node.n)
    def visit_LitString(self, node):
        self.outp.puts(node.s)
    def visit_dot_syntax(self, node):
        self.outp.puts('.syntax')
        self.outp.puts(node.n)
    def visit_stmt_inline(self, node):
        self.outp.puts(node.s)
        if node.vargq is not None:
            self.outp.puts('(')
            node.vargq.walkabout(self)
            self.outp.puts(')')
        self.outp.puts('::')
        node.v.walkabout(self)
    def visit_stmt_tax(self, node):
        self.outp.puts(node.s)
        if node.vq is not None:
            self.outp.puts('(')
            node.vq.walkabout(self)
            self.outp.puts(')')
        self.outp.puts(':')
        node.v.walkabout(self)
    def visit_args(self, node):
        tem1 = 0
        for tem2 in node.vlst:
            if tem1 > 0:
                self.outp.puts(',')
            tem1 = 1
            tem2.walkabout(self)
    def visit_arg(self, node):
        self.outp.puts(node.s)
        if node.sq is not None:
            self.outp.lnk()
            self.outp.puts(node.sq)
    def visit_protoGroup(self, node):
        self.outp.puts(node.n)
        self.outp.puts('{')
        self.outp.newline()
        for tem1 in node.vlst:
            tem1.walkabout(self)
            self.outp.newline()
        self.outp.puts('}')
    def visit_Module(self, node):
        for tem1 in node.vlst:
            tem1.walkabout(self)
            self.outp.newline()


class Parser(Parser00):

    def __init__(self, srctxt):
        Parser00.__init__(self, srctxt)

        self.ignore_wspace = IgnoreCls(' \t', ['/\\*(.|\\n)*?\\*/'])
        self.ignore_crlf = IgnoreCls(' \t\n', ['//.*', '/\\*(.|\\n)*?\\*/'])
        self.ignore_no = IgnoreCls('', [])
        
        self.lex_NEWLINE = HowRe('\\n+')
        self.lex_NAME = HowRe('[A-Za-z_][A-Za-z0-9_]*')
        self.lex_STRING = HowRe("'.*?'")
    
    def handle_NEWLINE(self):
        return self.handle_Lex(self.lex_NEWLINE)
    
    def handle_NAME(self, s = None):
        return self.handle_Lex(self.lex_NAME, s)
    
    def handle_STRING(self):
        s = self.handle_Lex(self.lex_STRING)
        return tostr_liud_STRING(s)

    def hdl_taxvalue(self):
        v = self.handle_opt2()
        if v is not None:
            return v
        v = self.handle_choices()
        if v is not None:
            return v
        return self.handle_OtherSyntax()

    def handle_opt2(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('^-') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_strings()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return liud_opt2(s, vlst)

    def handle_choices(self):
        sav0 = self.getpos()
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_taxone()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_crlf)
            if not self.handle_OpChar('|'):
                break
            self.SkipComments(self.ignore_wspace)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        if len(vlst) == 1:
            return vlst[0]
        return liud_choices(vlst)

    def handle_OtherSyntax(self):
        sav0 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('$NewSyntax') is None:
            self.setpos(sav0)
            return None
        return liud_OtherSyntax()

    def hdl_strings(self):
        v = self.handle_stringchoice()
        if v is not None:
            return v
        return self.handle_LitString()

    def handle_stringchoice(self):
        sav0 = self.getpos()
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        slst = []
        sav1 = self.getpos()
        while True:
            v3 = self.handle_STRING()
            if v3 is None:
                break
            slst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
            if not self.handle_OpChar('|'):
                break
            self.SkipComments(self.ignore_wspace)
        if not slst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return liud_stringchoice(slst)

    def hdl_taxone(self):
        v = self.handle_inline()
        if v is not None:
            return v
        return self.handle_serie()

    def handle_inline(self):
        sav0 = self.getpos()
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        v = self.handle_stmt_tax()
        if v is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return liud_inline(v)

    def handle_serie(self):
        sav0 = self.getpos()
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_baseitem()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        if len(vlst) == 1:
            return vlst[0]
        return liud_serie(vlst)

    def hdl_base0(self):
        v = self.handle_bracegroup()
        if v is not None:
            return v
        v = self.handle_bracechoice()
        if v is not None:
            return v
        v = self.handle_LitName()
        if v is not None:
            return v
        v = self.handle_LitString()
        if v is not None:
            return v
        return self.handle_ident()

    def handle_bracegroup(self):
        sav0 = self.getpos()
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_base0()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return liud_bracegroup(vlst)

    def handle_bracechoice(self):
        sav0 = self.getpos()
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_base0()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
            if not self.handle_OpChar('|'):
                break
            self.SkipComments(self.ignore_wspace)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return liud_bracechoice(vlst)

    def handle_ident(self):
        sav0 = self.getpos()
        s = self.handle_OpChar('+ident')
        if s is None:
            s = self.handle_OpChar('=ident')
        if s is None:
            s = self.handle_OpChar('-ident')
        if s is None:
            self.setpos(sav0)
            return None
        return liud_ident(s)

    def hdl_base1(self):
        v = self.handle_basestrn()
        if v is not None:
            return v
        return self.hdl_base0()

    def handle_basestrn(self):
        sav0 = self.getpos()
        v = self.hdl_strings()
        if v is None:
            v = self.handle_LitName()
        if v is None:
            self.setpos(sav0)
            return None
        if self.handle_OpChar('$') is None:
            self.setpos(sav0)
            return None
        return liud_basestrn(v)

    def hdl_baseitem(self):
        v = self.handle_syntaxdef()
        if v is not None:
            return v
        v = self.handle_ifnext()
        if v is not None:
            return v
        v = self.handle_ifnotnext()
        if v is not None:
            return v
        v = self.handle_itemq()
        if v is not None:
            return v
        v = self.handle_itemd()
        if v is not None:
            return v
        v = self.handle_itemp()
        if v is not None:
            return v
        v = self.handle_jiad()
        if v is not None:
            return v
        v = self.handle_jiap()
        if v is not None:
            return v
        v = self.handle_optgroup()
        if v is not None:
            return v
        return self.hdl_base1()

    def handle_ifnext(self):
        sav0 = self.getpos()
        if self.handle_OpChar('-ifnext(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        slst = []
        sav1 = self.getpos()
        while True:
            v3 = self.handle_STRING()
            if v3 is None:
                break
            slst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
            if not self.handle_OpChar('|'):
                break
            self.SkipComments(self.ignore_wspace)
        if not slst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return liud_ifnext(slst)

    def handle_ifnotnext(self):
        sav0 = self.getpos()
        if self.handle_OpChar('-ifnotnext(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        slst = []
        sav1 = self.getpos()
        while True:
            v3 = self.handle_STRING()
            if v3 is None:
                break
            slst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
            if not self.handle_OpChar('|'):
                break
            self.SkipComments(self.ignore_wspace)
        if not slst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return liud_ifnotnext(slst)

    def handle_itemq(self):
        sav0 = self.getpos()
        v = self.hdl_base1()
        if v is None:
            self.setpos(sav0)
            return None
        if self.handle_OpChar('?') is None:
            self.setpos(sav0)
            return None
        return liud_itemq(v)

    def handle_itemd(self):
        sav0 = self.getpos()
        v = self.hdl_base1()
        if v is None:
            self.setpos(sav0)
            return None
        if self.handle_OpChar('*') is None:
            self.setpos(sav0)
            return None
        return liud_itemd(v)

    def handle_itemp(self):
        sav0 = self.getpos()
        v = self.hdl_base0()
        if v is None:
            self.setpos(sav0)
            return None
        if self.handle_OpChar('+') is None:
            self.setpos(sav0)
            return None
        return liud_itemp(v)

    def handle_jiad(self):
        sav0 = self.getpos()
        v1 = self.hdl_base0()
        if v1 is None:
            self.setpos(sav0)
            return None
        sav1 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        v2q = self.handle_syntaxdef()
        if v2q is None:
            self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('^*') is None:
            self.setpos(sav0)
            return None
        sav2 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        v3q = self.handle_syntaxdef()
        if v3q is None:
            self.setpos(sav2)
        self.SkipComments(self.ignore_wspace)
        v4 = self.hdl_base1()
        if v4 is None:
            self.setpos(sav0)
            return None
        return liud_jiad(v1, v2q, v3q, v4)

    def handle_jiap(self):
        sav0 = self.getpos()
        v1 = self.hdl_base0()
        if v1 is None:
            self.setpos(sav0)
            return None
        sav1 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        v2q = self.handle_syntaxdef()
        if v2q is None:
            self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('^+') is None:
            self.setpos(sav0)
            return None
        sav2 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        v3q = self.handle_syntaxdef()
        if v3q is None:
            self.setpos(sav2)
        self.SkipComments(self.ignore_wspace)
        v4 = self.hdl_base1()
        if v4 is None:
            self.setpos(sav0)
            return None
        return liud_jiap(v1, v2q, v3q, v4)

    def handle_optgroup(self):
        sav0 = self.getpos()
        if self.handle_OpChar('[') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_base0()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(']') is None:
            self.setpos(sav0)
            return None
        return liud_optgroup(vlst)

    def handle_syntaxdef(self):
        sav0 = self.getpos()
        if self.handle_OpChar('-(') is None:
            self.setpos(sav0)
            return None
        n = self.handle_NAME()
        if n is None:
            self.setpos(sav0)
            return None
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return liud_syntaxdef(n)

    def handle_LitName(self):
        sav0 = self.getpos()
        n = self.handle_NAME()
        if n is None:
            self.setpos(sav0)
            return None
        return liud_LitName(n)

    def handle_LitString(self):
        sav0 = self.getpos()
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        return liud_LitString(s)

    def hdl_stmt(self):
        sav0 = self.getpos()
        v = self.hdl_stmtone()
        if v is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_NEWLINE() is None:
            self.setpos(sav0)
            return None
        return v

    def hdl_stmtone(self):
        v = self.handle_dot_syntax()
        if v is not None:
            return v
        v = self.handle_stmt_inline()
        if v is not None:
            return v
        v = self.handle_stmt_tax()
        if v is not None:
            return v
        return self.handle_protoGroup()

    def handle_dot_syntax(self):
        sav0 = self.getpos()
        if self.handle_OpChar('.syntax') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        n = self.handle_NAME()
        if n is None:
            self.setpos(sav0)
            return None
        return liud_dot_syntax(n)

    def handle_stmt_inline(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        flag = True
        sav1 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('(') is None:
            flag = False
        vargq = None
        if flag:
            self.SkipComments(self.ignore_wspace)
            vargq = self.handle_arg()
            if vargq is None:
                flag = False
        if flag:
            self.SkipComments(self.ignore_wspace)
            if self.handle_OpChar(')') is None:
                flag = False
        if not flag:
            vargq = None
            self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('::') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        v = self.hdl_taxvalue()
        if v is None:
            self.setpos(sav0)
            return None
        return liud_stmt_inline(s, vargq, v)

    def handle_stmt_tax(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        flag = True
        sav1 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('(') is None:
            flag = False
        vq = None
        if flag:
            self.SkipComments(self.ignore_wspace)
            vq = self.handle_args()
            if vq is None:
                flag = False
        if flag:
            self.SkipComments(self.ignore_wspace)
            if self.handle_OpChar(')') is None:
                flag = False
        if not flag:
            vq = None
            self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(':') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        v = self.hdl_taxvalue()
        if v is None:
            self.setpos(sav0)
            return None
        return liud_stmt_tax(s, vq, v)

    def handle_args(self):
        sav0 = self.getpos()
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.handle_arg()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
            if not self.handle_OpChar(','):
                break
            self.SkipComments(self.ignore_wspace)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        return liud_args(vlst)

    def handle_arg(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        sq = self.handle_OpChar('?')
        if sq is None:
            sq = self.handle_OpChar('*')
        return liud_arg(s, sq)

    def handle_protoGroup(self):
        sav0 = self.getpos()
        n = self.handle_NAME()
        if n is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_crlf)
        if self.handle_OpChar('{') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_crlf)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_stmt()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_crlf)
        self.setpos(sav1)
        self.SkipComments(self.ignore_crlf)
        if self.handle_OpChar('}') is None:
            self.setpos(sav0)
            return None
        return liud_protoGroup(n, vlst)

    def handle_Module(self):
        self.SkipComments(self.ignore_crlf)
        sav0 = self.getpos()
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_stmt()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_crlf)
        self.setpos(sav1)
        self.SkipComments(self.ignore_crlf)
        if self.handle_ENDMARKER() is None:
            self.setpos(sav0)
            return None
        return liud_Module(vlst)

def Test_Parse_liud(srctxt):
    parser = Parser(srctxt)
    mod = parser.handle_Module()
    if mod is None:
        lastpos, lastlineno, lastcolumn, lastline = parser.GetLast()
        print 'parse error, last pos = %d' % lastpos
        print 'last lineno = %d, column = %d' % (lastlineno, lastcolumn)
        print 'last line :', lastline
    else:
        print 'parse success'
    return mod


def Test_Out_liud(mod):
    outp = OutPrt()
    the = liud_out_visitor_01(outp)
    mod.walkabout(the)
    outp.newline()

s_sample_liud = '''
.syntax wspace

iLiuDExpr {
taxvalue :: ( opt2(s,vlst*) : NAME '^-' '(' strings+ ')' )
    | ( choices(vlst*) : taxone -(crlf) ^+ '|' )
    | ( OtherSyntax : '$NewSyntax' )
    strings :: ( stringchoice(slst*) : '(' STRING ^+ '|' ')' )
        | LitString
    taxone :: ( inline : '(' stmt_tax ')' )
        | ( serie(vlst*) : baseitem+ )
        base0 :: ( bracegroup(vlst*) : '(' base0+ ')' )
            | ( bracechoice(vlst*) : '(' base0 ^+ '|' ')' )
            | LitName
            | LitString
            | ( ident : ('+ident' | '=ident' | '-ident')$ )
        base1 :: ( basestrn : (strings | LitName) -(no) '$' )
            | base0
        baseitem :: syntaxdef
            | ( ifnext(slst*) : '-ifnext(' STRING ^+ '|' ')' )
            | ( ifnotnext(slst*) : '-ifnotnext(' STRING ^+ '|' ')' )
            | ( itemq : base1 -(no) '?' )
            | ( itemd : base1 -(no) '*' )
            | ( itemp : base0 -(no) '+' )
            | ( jiad(v1,v2q?,v3q?,v4) : base0 syntaxdef? '^*' syntaxdef? base1 )
            | ( jiap(v1,v2q?,v3q?,v4) : base0 syntaxdef? '^+' syntaxdef? base1 )
            | ( optgroup(vlst*) : '[' base0+ ']' )
            | base1
            syntaxdef : '-(' -(no) NAME -(no) ')'
        LitName : NAME
        LitString : STRING
}
stmt :: stmtone NEWLINE$
    stmtone :: ( dot_syntax : '.syntax' NAME )
        | stmt_inline
        | stmt_tax
        | protoGroup

stmt_inline(s, vargq?, v) : NAME ['(' arg ')'] '::' taxvalue
stmt_tax(s, vq?, v) : NAME ['(' args ')'] ':' taxvalue
    args(vlst*) : arg ^+ ',' -(no)
        arg(s, sq?) : NAME -(no) ('?' | '*')$?

.syntax crlf
protoGroup : NAME '{' stmt* '}'
Module(vlst*) : stmt* ENDMARKER$

'''

if __name__ == '__main__':
    mod = Test_Parse_liud(s_sample_liud)
    if mod :
        Test_Out_liud(mod)
    
