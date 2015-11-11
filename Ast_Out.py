# auto generate code, LiuTaoTao

from lib import *

class Out_stmtone:
    def __init__(self, s, vlst):
        self.s = s
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_stmtone(self)


class Out_Jiad:
    def __init__(self, v1, vq, v2):
        self.v1 = v1
        self.vq = vq
        self.v2 = v2

    def walkabout(self, visitor):
        return visitor.visit_Jiad(self)


class Out_String:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_String(self)


class Out_optgroup:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_optgroup(self)


class Out_itemd:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_itemd(self)


class Out_ident:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_ident(self)


class Out_newline:

    def walkabout(self, visitor):
        return visitor.visit_newline(self)


class Out_lnk:

    def walkabout(self, visitor):
        return visitor.visit_lnk(self)


class Out_Xlst:

    def walkabout(self, visitor):
        return visitor.visit_Xlst(self)


class Out_Xchoice:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def walkabout(self, visitor):
        return visitor.visit_Xchoice(self)


class Out_Xif:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_Xif(self)


class Out_Xq:

    def walkabout(self, visitor):
        return visitor.visit_Xq(self)


class Out_X:

    def walkabout(self, visitor):
        return visitor.visit_X(self)


class Out_Module:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_Module(self)

class Out_sample_visitor_00:
    def visit_stmtone(self, node): pass
    def visit_Jiad(self, node): pass
    def visit_String(self, node): pass
    def visit_optgroup(self, node): pass
    def visit_itemd(self, node): pass
    def visit_ident(self, node): pass
    def visit_newline(self, node): pass
    def visit_lnk(self, node): pass
    def visit_Xlst(self, node): pass
    def visit_Xchoice(self, node): pass
    def visit_Xif(self, node): pass
    def visit_Xq(self, node): pass
    def visit_X(self, node): pass
    def visit_Module(self, node): pass

class Out_sample_visitor_01:
    def visit_stmtone(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_Jiad(self, node):
        node.v1.walkabout(self)
        if node.vq is not None:
            node.vq.walkabout(self)
        node.v2.walkabout(self)
    def visit_String(self, node):
        pass
    def visit_optgroup(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_itemd(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_ident(self, node):
        pass
    def visit_newline(self, node):
        pass
    def visit_lnk(self, node):
        pass
    def visit_Xlst(self, node):
        pass
    def visit_Xchoice(self, node):
        pass
    def visit_Xif(self, node):
        pass
    def visit_Xq(self, node):
        pass
    def visit_X(self, node):
        pass
    def visit_Module(self, node):
        for v in node.vlst:
            v.walkabout(self)

class Out_out_visitor_01:
    def __init__(self, outp):
        self.outp = outp
    def visit_stmtone(self, node):
        self.outp.puts(node.s)
        self.outp.puts(':')
        for tem1 in node.vlst:
            tem1.walkabout(self)
    def visit_Jiad(self, node):
        node.v1.walkabout(self)
        if node.vq is not None:
            node.vq.walkabout(self)
        self.outp.puts('^*')
        node.v2.walkabout(self)
    def visit_String(self, node):
        self.outp.puts(node.s)
    def visit_optgroup(self, node):
        self.outp.puts('[')
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.puts(']')
    def visit_itemd(self, node):
        self.outp.puts('(')
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.puts(')*')
    def visit_ident(self, node):
        self.outp.puts(node.s)
    def visit_newline(self, node):
        self.outp.puts('NL')
    def visit_lnk(self, node):
        self.outp.puts('-')
    def visit_Xlst(self, node):
        self.outp.puts('x*')
    def visit_Xchoice(self, node):
        self.outp.puts('x?(')
        self.outp.puts(node.s1)
        self.outp.puts(',')
        self.outp.puts(node.s2)
        self.outp.puts(')')
    def visit_Xif(self, node):
        self.outp.puts('x?(')
        self.outp.puts(node.s)
        self.outp.puts(')')
    def visit_Xq(self, node):
        self.outp.puts('x?')
    def visit_X(self, node):
        self.outp.puts('x')
    def visit_Module(self, node):
        for tem1 in node.vlst:
            tem1.walkabout(self)
            self.outp.newline()


class Parser(Parser00):

    def __init__(self, srctxt):
        Parser00.__init__(self, srctxt)

        self.ignore_wspace = IgnoreCls(' \t', ['/\\*(.|\\n)*?\\*/'])
        self.ignore_crlf = IgnoreCls(' \t\n', ['//.*', '/\\*(.|\\n)*?\\*/'])
        
        self.lex_NEWLINE = HowRe('\\n+')
        self.lex_NAME = HowRe('[A-Za-z_][A-Za-z0-9_]*')
        self.lex_STRING = HowRe("'(.|\\n)*?'")
    
    def handle_NEWLINE(self):
        return self.handle_Lex(self.lex_NEWLINE)
    
    def handle_NAME(self, s = None):
        return self.handle_Lex(self.lex_NAME, s)
    
    def handle_STRING(self):
        s = self.handle_Lex(self.lex_STRING)
        return tostr_Out_STRING(s)

    def hdl_stmt(self):
        sav0 = self.getpos()
        v = self.handle_stmtone()
        if v is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_NEWLINE() is None:
            self.setpos(sav0)
            return None
        return v

    def handle_stmtone(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(':') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_item()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.SkipComments(self.ignore_wspace)
        self.setpos(sav1)
        return Out_stmtone(s, vlst)

    def hdl_item(self):
        v = self.handle_Jiad()
        if v is not None:
            return v
        v = self.handle_String()
        if v is not None:
            return v
        v = self.handle_optgroup()
        if v is not None:
            return v
        v = self.handle_itemd()
        if v is not None:
            return v
        v = self.handle_ident()
        if v is not None:
            return v
        v = self.handle_newline()
        if v is not None:
            return v
        v = self.handle_lnk()
        if v is not None:
            return v
        v = self.handle_Xlst()
        if v is not None:
            return v
        v = self.handle_Xchoice()
        if v is not None:
            return v
        v = self.handle_Xif()
        if v is not None:
            return v
        v = self.handle_Xq()
        if v is not None:
            return v
        return self.handle_X()

    def handle_Jiad(self):
        sav0 = self.getpos()
        v1 = self.handle_X()
        if v1 is None:
            self.setpos(sav0)
            return None
        sav1 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        vq = self.handle_lnk()
        if vq is None:
            self.setpos(sav1)
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('^*') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        v2 = self.handle_String()
        if v2 is None:
            v2 = self.handle_X()
        if v2 is None:
            self.setpos(sav0)
            return None
        return Out_Jiad(v1, vq, v2)

    def handle_String(self):
        sav0 = self.getpos()
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        return Out_String(s)

    def handle_optgroup(self):
        sav0 = self.getpos()
        if self.handle_OpChar('[') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_item()
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
        return Out_optgroup(vlst)

    def handle_itemd(self):
        sav0 = self.getpos()
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_item()
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
        if self.handle_OpChar(')*') is None:
            self.setpos(sav0)
            return None
        return Out_itemd(vlst)

    def handle_ident(self):
        sav0 = self.getpos()
        s = self.handle_OpChar('+ident')
        if s is None:
            s = self.handle_OpChar('-ident')
        if s is None:
            self.setpos(sav0)
            return None
        return Out_ident(s)

    def handle_newline(self):
        sav0 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        if self.handle_NAME('NL') is None:
            self.setpos(sav0)
            return None
        return Out_newline()

    def handle_lnk(self):
        sav0 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('-') is None:
            self.setpos(sav0)
            return None
        return Out_lnk()

    def handle_Xlst(self):
        sav0 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('x*') is None:
            self.setpos(sav0)
            return None
        return Out_Xlst()

    def handle_Xchoice(self):
        sav0 = self.getpos()
        if self.handle_OpChar('x?(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        s1 = self.handle_STRING()
        if s1 is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(',') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        s2 = self.handle_STRING()
        if s2 is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return Out_Xchoice(s1, s2)

    def handle_Xif(self):
        sav0 = self.getpos()
        if self.handle_OpChar('x?(') is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return Out_Xif(s)

    def handle_Xq(self):
        sav0 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        if self.handle_OpChar('x?') is None:
            self.setpos(sav0)
            return None
        return Out_Xq()

    def handle_X(self):
        sav0 = self.getpos()
        self.SkipComments(self.ignore_wspace)
        if self.handle_NAME('x') is None:
            self.setpos(sav0)
            return None
        return Out_X()

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
        return Out_Module(vlst)

def Test_Parse_Out(srctxt):
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


def Test_Out_Out(mod):
    outp = OutPrt()
    the = Out_out_visitor_01(outp)
    mod.walkabout(the)
    outp.newline()

s_sample_Out = '''
Module : (x NL)*
stmtone : x ':' x*
Jiad : x x? '^*' x
String : x
optgroup : '[' x* ']'
itemd : '(' x* ')*'
ident : x
newline : 'NL'
lnk : '-'
Xlst : 'x*'
Xchoice : 'x?(' x ',' x ')'
Xif : 'x?(' x ')'
Xq : 'x?'
X : 'x'
'''

if __name__ == '__main__':
    mod = Test_Parse_Out(s_sample_Out)
    if mod :
        Test_Out_Out(mod)
    
