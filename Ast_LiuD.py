# auto generate code, LiuTaoTao

from lib import *

class LiuD_string_def:
    def __init__(self, n1, n2, s):
        self.n1 = n1
        self.n2 = n2
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_string_def(self)


class LiuD_opt2:
    def __init__(self, s, vlst):
        self.s = s
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_opt2(self)


class LiuD_choices:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_choices(self)


class LiuD_MoreDef:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_MoreDef(self)


class LiuD_OtherSyntax:

    def walkabout(self, visitor):
        return visitor.visit_OtherSyntax(self)


class LiuD_stringchoice:
    def __init__(self, slst):
        self.slst = slst

    def walkabout(self, visitor):
        return visitor.visit_stringchoice(self)


class LiuD_inline:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_inline(self)


class LiuD_serie:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_serie(self)


class LiuD_bracegroup:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_bracegroup(self)


class LiuD_bracechoice:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_bracechoice(self)


class LiuD_BoolChoice:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def walkabout(self, visitor):
        return visitor.visit_BoolChoice(self)


class LiuD_BoolIf:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_BoolIf(self)


class LiuD_ident:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_ident(self)


class LiuD_basestrn:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_basestrn(self)


class LiuD_ifnext:
    def __init__(self, slst):
        self.slst = slst

    def walkabout(self, visitor):
        return visitor.visit_ifnext(self)


class LiuD_ifnotnext:
    def __init__(self, slst):
        self.slst = slst

    def walkabout(self, visitor):
        return visitor.visit_ifnotnext(self)


class LiuD_itemq:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_itemq(self)


class LiuD_itemd:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_itemd(self)


class LiuD_itemp:
    def __init__(self, v):
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_itemp(self)


class LiuD_jiad:
    def __init__(self, v1, v2q, v3q, v4):
        self.v1 = v1
        self.v2q = v2q
        self.v3q = v3q
        self.v4 = v4

    def walkabout(self, visitor):
        return visitor.visit_jiad(self)


class LiuD_jiap:
    def __init__(self, v1, v2q, v3q, v4):
        self.v1 = v1
        self.v2q = v2q
        self.v3q = v3q
        self.v4 = v4

    def walkabout(self, visitor):
        return visitor.visit_jiap(self)


class LiuD_optgroup:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_optgroup(self)


class LiuD_syntaxdef:
    def __init__(self, n):
        self.n = n

    def walkabout(self, visitor):
        return visitor.visit_syntaxdef(self)


class LiuD_noskip:

    def walkabout(self, visitor):
        return visitor.visit_noskip(self)


class LiuD_LitName:
    def __init__(self, n):
        self.n = n

    def walkabout(self, visitor):
        return visitor.visit_LitName(self)


class LiuD_LitString:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_LitString(self)


class LiuD_dot_syntax:
    def __init__(self, n):
        self.n = n

    def walkabout(self, visitor):
        return visitor.visit_dot_syntax(self)


class LiuD_set_linecomment:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_set_linecomment(self)


class LiuD_set_blockcomment:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def walkabout(self, visitor):
        return visitor.visit_set_blockcomment(self)


class LiuD_name_prefix:
    def __init__(self, n):
        self.n = n

    def walkabout(self, visitor):
        return visitor.visit_name_prefix(self)


class LiuD_sample_text:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_sample_text(self)


class LiuD_stmt_inline:
    def __init__(self, s, vargq, v):
        self.s = s
        self.vargq = vargq
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_stmt_inline(self)


class LiuD_stmt_tax:
    def __init__(self, s, vq, v):
        self.s = s
        self.vq = vq
        self.v = v

    def walkabout(self, visitor):
        return visitor.visit_stmt_tax(self)


class LiuD_args:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_args(self)


class LiuD_arg:
    def __init__(self, s, sq):
        self.s = s
        self.sq = sq

    def walkabout(self, visitor):
        return visitor.visit_arg(self)


class LiuD_output_rules:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_output_rules(self)


class LiuD_orule:
    def __init__(self, s, vlst):
        self.s = s
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_orule(self)


class LiuD_oJiad:
    def __init__(self, v1, vq, v2):
        self.v1 = v1
        self.vq = vq
        self.v2 = v2

    def walkabout(self, visitor):
        return visitor.visit_oJiad(self)


class LiuD_oString:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_oString(self)


class LiuD_ooptgroup:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_ooptgroup(self)


class LiuD_oitemd:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_oitemd(self)


class LiuD_oident:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_oident(self)


class LiuD_onewline:

    def walkabout(self, visitor):
        return visitor.visit_onewline(self)


class LiuD_olnk:

    def walkabout(self, visitor):
        return visitor.visit_olnk(self)


class LiuD_oXlst:

    def walkabout(self, visitor):
        return visitor.visit_oXlst(self)


class LiuD_oXchoice:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def walkabout(self, visitor):
        return visitor.visit_oXchoice(self)


class LiuD_oXif:
    def __init__(self, s):
        self.s = s

    def walkabout(self, visitor):
        return visitor.visit_oXif(self)


class LiuD_oXq:

    def walkabout(self, visitor):
        return visitor.visit_oXq(self)


class LiuD_oX:

    def walkabout(self, visitor):
        return visitor.visit_oX(self)


class LiuD_protoGroup:
    def __init__(self, n, vlst):
        self.n = n
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_protoGroup(self)


class LiuD_Module:
    def __init__(self, vlst):
        self.vlst = vlst

    def walkabout(self, visitor):
        return visitor.visit_Module(self)

class LiuD_sample_visitor_00:
    def visit_string_def(self, node): pass
    def visit_opt2(self, node): pass
    def visit_choices(self, node): pass
    def visit_MoreDef(self, node): pass
    def visit_OtherSyntax(self, node): pass
    def visit_stringchoice(self, node): pass
    def visit_inline(self, node): pass
    def visit_serie(self, node): pass
    def visit_bracegroup(self, node): pass
    def visit_bracechoice(self, node): pass
    def visit_BoolChoice(self, node): pass
    def visit_BoolIf(self, node): pass
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
    def visit_noskip(self, node): pass
    def visit_LitName(self, node): pass
    def visit_LitString(self, node): pass
    def visit_dot_syntax(self, node): pass
    def visit_set_linecomment(self, node): pass
    def visit_set_blockcomment(self, node): pass
    def visit_name_prefix(self, node): pass
    def visit_sample_text(self, node): pass
    def visit_stmt_inline(self, node): pass
    def visit_stmt_tax(self, node): pass
    def visit_args(self, node): pass
    def visit_arg(self, node): pass
    def visit_output_rules(self, node): pass
    def visit_orule(self, node): pass
    def visit_oJiad(self, node): pass
    def visit_oString(self, node): pass
    def visit_ooptgroup(self, node): pass
    def visit_oitemd(self, node): pass
    def visit_oident(self, node): pass
    def visit_onewline(self, node): pass
    def visit_olnk(self, node): pass
    def visit_oXlst(self, node): pass
    def visit_oXchoice(self, node): pass
    def visit_oXif(self, node): pass
    def visit_oXq(self, node): pass
    def visit_oX(self, node): pass
    def visit_protoGroup(self, node): pass
    def visit_Module(self, node): pass

class LiuD_sample_visitor_01:
    def visit_string_def(self, node):
        pass
    def visit_opt2(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_choices(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_MoreDef(self, node):
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
    def visit_BoolChoice(self, node):
        pass
    def visit_BoolIf(self, node):
        pass
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
    def visit_noskip(self, node):
        pass
    def visit_LitName(self, node):
        pass
    def visit_LitString(self, node):
        pass
    def visit_dot_syntax(self, node):
        pass
    def visit_set_linecomment(self, node):
        pass
    def visit_set_blockcomment(self, node):
        pass
    def visit_name_prefix(self, node):
        pass
    def visit_sample_text(self, node):
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
    def visit_output_rules(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_orule(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_oJiad(self, node):
        node.v1.walkabout(self)
        if node.vq is not None:
            node.vq.walkabout(self)
        node.v2.walkabout(self)
    def visit_oString(self, node):
        pass
    def visit_ooptgroup(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_oitemd(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_oident(self, node):
        pass
    def visit_onewline(self, node):
        pass
    def visit_olnk(self, node):
        pass
    def visit_oXlst(self, node):
        pass
    def visit_oXchoice(self, node):
        pass
    def visit_oXif(self, node):
        pass
    def visit_oXq(self, node):
        pass
    def visit_oX(self, node):
        pass
    def visit_protoGroup(self, node):
        for v in node.vlst:
            v.walkabout(self)
    def visit_Module(self, node):
        for v in node.vlst:
            v.walkabout(self)

class LiuD_out_visitor_01:
    def __init__(self, outp):
        self.outp = outp
    def visit_string_def(self, node):
        self.outp.puts('.string')
        self.outp.puts(node.n1)
        self.outp.puts(node.n2)
        self.outp.putss(node.s)
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
    def visit_MoreDef(self, node):
        self.outp.puts('+')
        self.outp.lnk()
        for tem1 in node.vlst:
            tem1.walkabout(self)
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
    def visit_BoolChoice(self, node):
        self.outp.puts('Bool(')
        self.outp.putss(node.s1)
        self.outp.puts(',')
        self.outp.putss(node.s2)
        self.outp.puts(')')
    def visit_BoolIf(self, node):
        self.outp.puts('Bool(')
        self.outp.putss(node.s)
        self.outp.puts(')')
    def visit_ident(self, node):
        self.outp.putss(node.s)
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
    def visit_noskip(self, node):
        self.outp.puts('-')
    def visit_LitName(self, node):
        self.outp.puts(node.n)
    def visit_LitString(self, node):
        self.outp.putss(node.s)
    def visit_dot_syntax(self, node):
        self.outp.puts('.syntax')
        self.outp.puts(node.n)
    def visit_set_linecomment(self, node):
        self.outp.puts('.set_linecomment')
        self.outp.putss(node.s)
    def visit_set_blockcomment(self, node):
        self.outp.puts('.set_blockcomment')
        self.outp.putss(node.s1)
        self.outp.putss(node.s2)
    def visit_name_prefix(self, node):
        self.outp.puts('.name_prefix')
        self.outp.puts(node.n)
    def visit_sample_text(self, node):
        self.outp.puts('Sample Text =')
        self.outp.putss(node.s)
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
    def visit_output_rules(self, node):
        self.outp.puts('OutPut')
        self.outp.puts('Rules')
        self.outp.puts('{')
        self.outp.newline()
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.puts('}')
    def visit_orule(self, node):
        self.outp.puts(node.s)
        self.outp.puts(':')
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.newline()
    def visit_oJiad(self, node):
        node.v1.walkabout(self)
        if node.vq is not None:
            node.vq.walkabout(self)
        self.outp.puts('^*')
        node.v2.walkabout(self)
    def visit_oString(self, node):
        self.outp.putss(node.s)
    def visit_ooptgroup(self, node):
        self.outp.puts('[')
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.puts(']')
    def visit_oitemd(self, node):
        self.outp.puts('(')
        for tem1 in node.vlst:
            tem1.walkabout(self)
        self.outp.puts(')*')
    def visit_oident(self, node):
        self.outp.putss(node.s)
    def visit_onewline(self, node):
        self.outp.puts('NL')
    def visit_olnk(self, node):
        self.outp.puts('-')
    def visit_oXlst(self, node):
        self.outp.puts('x*')
    def visit_oXchoice(self, node):
        self.outp.puts('x?(')
        self.outp.putss(node.s1)
        self.outp.puts(',')
        self.outp.putss(node.s2)
        self.outp.puts(')')
    def visit_oXif(self, node):
        self.outp.puts('x?(')
        self.outp.putss(node.s)
        self.outp.puts(')')
    def visit_oXq(self, node):
        self.outp.puts('x?')
    def visit_oX(self, node):
        self.outp.puts('x')
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

        self.skips = [
            IgnoreCls(' \t', ['\\/\\/.*', '/\\*(.|\\n)*?\\*/']),
            IgnoreCls(' \t\n', ['\\/\\/.*', '/\\*(.|\\n)*?\\*/']),
        ]

    def handle_string_def(self):
        sav0 = self.getpos()
        if self.handle_OpChar('.string') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        n1 = self.handle_NAME()
        if n1 is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        n2 = self.handle_NAME()
        if n2 is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        return LiuD_string_def(n1, n2, s)

    def hdl_taxvalue(self):
        v = self.handle_opt2()
        if v is not None:
            return v
        v = self.handle_choices()
        if v is not None:
            return v
        v = self.handle_MoreDef()
        if v is not None:
            return v
        return self.handle_OtherSyntax()

    def handle_opt2(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar('^-') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_strings()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_opt2(s, vlst)

    def handle_choices(self):
        tem1 = self.hdl_taxone()
        if tem1 is None:
            return None
        vlst = [tem1]
        while True:
            sav0 = self.getpos()
            self.Skip(1)
            if not self.handle_OpChar('|'):
                break
            self.Skip(0)
            v3 = self.hdl_taxone()
            if v3 is None:
                break
            vlst.append(v3)
        self.setpos(sav0)
        if len(vlst) == 1:
            return tem1
        return LiuD_choices(vlst)

    def handle_MoreDef(self):
        sav0 = self.getpos()
        if self.handle_OpChar('+') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_baseitem()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
        self.setpos(sav1)
        return LiuD_MoreDef(vlst)

    def handle_OtherSyntax(self):
        sav0 = self.getpos()
        self.Skip(0)
        if self.handle_OpChar('$NewSyntax') is None:
            self.setpos(sav0)
            return None
        return LiuD_OtherSyntax()

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
        self.Skip(0)
        slst = []
        sav1 = self.getpos()
        while True:
            v3 = self.handle_STRING()
            if v3 is None:
                break
            slst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
            if not self.handle_OpChar('|'):
                break
            self.Skip(0)
        if not slst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_stringchoice(slst)

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
        self.Skip(0)
        v = self.handle_stmt_tax()
        if v is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_inline(v)

    def handle_serie(self):
        tem1 = self.hdl_baseitem()
        if tem1 is None:
            return None
        vlst = [tem1]
        while True:
            sav0 = self.getpos()
            self.Skip(0)
            v3 = self.hdl_baseitem()
            if v3 is None:
                break
            vlst.append(v3)
        self.setpos(sav0)
        if len(vlst) == 1:
            return tem1
        return LiuD_serie(vlst)

    def hdl_base0(self):
        v = self.handle_bracegroup()
        if v is not None:
            return v
        v = self.handle_bracechoice()
        if v is not None:
            return v
        v = self.handle_BoolChoice()
        if v is not None:
            return v
        v = self.handle_BoolIf()
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
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_base0()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_bracegroup(vlst)

    def handle_bracechoice(self):
        sav0 = self.getpos()
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_base1()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
            if not self.handle_OpChar('|'):
                break
            self.Skip(0)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_bracechoice(vlst)

    def handle_BoolChoice(self):
        sav0 = self.getpos()
        if self.handle_OpChar('Bool(') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s1 = self.handle_STRING()
        if s1 is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar(',') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s2 = self.handle_STRING()
        if s2 is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_BoolChoice(s1, s2)

    def handle_BoolIf(self):
        sav0 = self.getpos()
        if self.handle_OpChar('Bool(') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_BoolIf(s)

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
        return LiuD_ident(s)

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
        return LiuD_basestrn(v)

    def hdl_baseitem(self):
        v = self.handle_ifnext()
        if v is not None:
            return v
        v = self.handle_ifnotnext()
        if v is not None:
            return v
        v = self.hdl_skipdef()
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
        self.Skip(0)
        slst = []
        sav1 = self.getpos()
        while True:
            v3 = self.handle_STRING()
            if v3 is None:
                break
            slst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
            if not self.handle_OpChar('|'):
                break
            self.Skip(0)
        if not slst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_ifnext(slst)

    def handle_ifnotnext(self):
        sav0 = self.getpos()
        if self.handle_OpChar('-ifnotnext(') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        slst = []
        sav1 = self.getpos()
        while True:
            v3 = self.handle_STRING()
            if v3 is None:
                break
            slst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
            if not self.handle_OpChar('|'):
                break
            self.Skip(0)
        if not slst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_ifnotnext(slst)

    def handle_itemq(self):
        sav0 = self.getpos()
        v = self.hdl_base1()
        if v is None:
            self.setpos(sav0)
            return None
        if self.handle_OpChar('?') is None:
            self.setpos(sav0)
            return None
        return LiuD_itemq(v)

    def handle_itemd(self):
        sav0 = self.getpos()
        v = self.hdl_base1()
        if v is None:
            self.setpos(sav0)
            return None
        if self.handle_OpChar('*') is None:
            self.setpos(sav0)
            return None
        return LiuD_itemd(v)

    def handle_itemp(self):
        sav0 = self.getpos()
        v = self.hdl_base0()
        if v is None:
            self.setpos(sav0)
            return None
        if self.handle_OpChar('+') is None:
            self.setpos(sav0)
            return None
        return LiuD_itemp(v)

    def handle_jiad(self):
        sav0 = self.getpos()
        v1 = self.hdl_base0()
        if v1 is None:
            self.setpos(sav0)
            return None
        sav1 = self.getpos()
        self.Skip(0)
        v2q = self.hdl_skipdef()
        if v2q is None:
            self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar('^*') is None:
            self.setpos(sav0)
            return None
        sav2 = self.getpos()
        self.Skip(0)
        v3q = self.hdl_skipdef()
        if v3q is None:
            self.setpos(sav2)
        self.Skip(0)
        v4 = self.hdl_base1()
        if v4 is None:
            self.setpos(sav0)
            return None
        return LiuD_jiad(v1, v2q, v3q, v4)

    def handle_jiap(self):
        sav0 = self.getpos()
        v1 = self.hdl_base0()
        if v1 is None:
            self.setpos(sav0)
            return None
        sav1 = self.getpos()
        self.Skip(0)
        v2q = self.hdl_skipdef()
        if v2q is None:
            self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar('^+') is None:
            self.setpos(sav0)
            return None
        sav2 = self.getpos()
        self.Skip(0)
        v3q = self.hdl_skipdef()
        if v3q is None:
            self.setpos(sav2)
        self.Skip(0)
        v4 = self.hdl_base1()
        if v4 is None:
            self.setpos(sav0)
            return None
        return LiuD_jiap(v1, v2q, v3q, v4)

    def handle_optgroup(self):
        sav0 = self.getpos()
        if self.handle_OpChar('[') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_base0()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(']') is None:
            self.setpos(sav0)
            return None
        return LiuD_optgroup(vlst)

    def hdl_skipdef(self):
        v = self.handle_syntaxdef()
        if v is not None:
            return v
        return self.handle_noskip()

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
        return LiuD_syntaxdef(n)

    def handle_noskip(self):
        sav0 = self.getpos()
        self.Skip(0)
        if self.handle_OpChar('-') is None:
            self.setpos(sav0)
            return None
        return LiuD_noskip()

    def handle_LitName(self):
        sav0 = self.getpos()
        n = self.handle_NAME()
        if n is None:
            self.setpos(sav0)
            return None
        return LiuD_LitName(n)

    def handle_LitString(self):
        sav0 = self.getpos()
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        return LiuD_LitString(s)

    def hdl_stmt(self):
        sav0 = self.getpos()
        v = self.hdl_stmtone()
        if v is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_NEWLINE() is None:
            self.setpos(sav0)
            return None
        return v

    def hdl_stmtone(self):
        v = self.handle_dot_syntax()
        if v is not None:
            return v
        v = self.handle_set_linecomment()
        if v is not None:
            return v
        v = self.handle_set_blockcomment()
        if v is not None:
            return v
        v = self.handle_name_prefix()
        if v is not None:
            return v
        v = self.handle_output_rules()
        if v is not None:
            return v
        v = self.handle_string_def()
        if v is not None:
            return v
        v = self.handle_sample_text()
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
        self.Skip(0)
        n = self.handle_NAME()
        if n is None:
            n = self.handle_OpChar('-')
        if n is None:
            self.setpos(sav0)
            return None
        return LiuD_dot_syntax(n)

    def handle_set_linecomment(self):
        sav0 = self.getpos()
        if self.handle_OpChar('.set_linecomment') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        return LiuD_set_linecomment(s)

    def handle_set_blockcomment(self):
        sav0 = self.getpos()
        if self.handle_OpChar('.set_blockcomment') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s1 = self.handle_STRING()
        if s1 is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s2 = self.handle_STRING()
        if s2 is None:
            self.setpos(sav0)
            return None
        return LiuD_set_blockcomment(s1, s2)

    def handle_name_prefix(self):
        sav0 = self.getpos()
        if self.handle_OpChar('.name_prefix') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        n = self.handle_NAME()
        if n is None:
            self.setpos(sav0)
            return None
        return LiuD_name_prefix(n)

    def handle_sample_text(self):
        sav0 = self.getpos()
        if self.handle_NAME('Sample') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_NAME('Text') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar('=') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        return LiuD_sample_text(s)

    def handle_stmt_inline(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        flag = True
        sav1 = self.getpos()
        self.Skip(0)
        if self.handle_OpChar('(') is None:
            flag = False
        vargq = None
        if flag:
            self.Skip(0)
            vargq = self.handle_arg()
            if vargq is None:
                flag = False
        if flag:
            self.Skip(0)
            if self.handle_OpChar(')') is None:
                flag = False
        if not flag:
            vargq = None
            self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar('::') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        v = self.hdl_taxvalue()
        if v is None:
            self.setpos(sav0)
            return None
        return LiuD_stmt_inline(s, vargq, v)

    def handle_stmt_tax(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        flag = True
        sav1 = self.getpos()
        self.Skip(0)
        if self.handle_OpChar('(') is None:
            flag = False
        vq = None
        if flag:
            self.Skip(0)
            vq = self.handle_args()
            if vq is None:
                flag = False
        if flag:
            self.Skip(0)
            if self.handle_OpChar(')') is None:
                flag = False
        if not flag:
            vq = None
            self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(':') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        v = self.hdl_taxvalue()
        if v is None:
            self.setpos(sav0)
            return None
        return LiuD_stmt_tax(s, vq, v)

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
            self.Skip(0)
            if not self.handle_OpChar(','):
                break
            self.Skip(0)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        return LiuD_args(vlst)

    def handle_arg(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        sq = self.handle_OpChar('?')
        if sq is None:
            sq = self.handle_OpChar('*')
        return LiuD_arg(s, sq)

    def handle_output_rules(self):
        sav0 = self.getpos()
        if self.handle_NAME('Output') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_NAME('Rules') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar('{') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        self.handle_NEWLINE()
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.handle_orule()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar('}') is None:
            self.setpos(sav0)
            return None
        return LiuD_output_rules(vlst)

    def handle_orule(self):
        sav0 = self.getpos()
        s = self.handle_NAME()
        if s is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar(':') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_oitem()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_NEWLINE() is None:
            self.setpos(sav0)
            return None
        return LiuD_orule(s, vlst)

    def hdl_oitem(self):
        v = self.handle_oJiad()
        if v is not None:
            return v
        v = self.handle_oString()
        if v is not None:
            return v
        v = self.handle_ooptgroup()
        if v is not None:
            return v
        v = self.handle_oitemd()
        if v is not None:
            return v
        v = self.handle_oident()
        if v is not None:
            return v
        v = self.handle_onewline()
        if v is not None:
            return v
        v = self.handle_olnk()
        if v is not None:
            return v
        v = self.handle_oXlst()
        if v is not None:
            return v
        v = self.handle_oXchoice()
        if v is not None:
            return v
        v = self.handle_oXif()
        if v is not None:
            return v
        v = self.handle_oXq()
        if v is not None:
            return v
        return self.handle_oX()

    def handle_oJiad(self):
        sav0 = self.getpos()
        v1 = self.handle_oX()
        if v1 is None:
            self.setpos(sav0)
            return None
        sav1 = self.getpos()
        self.Skip(0)
        vq = self.handle_olnk()
        if vq is None:
            self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar('^*') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        v2 = self.handle_oString()
        if v2 is None:
            v2 = self.handle_oX()
        if v2 is None:
            self.setpos(sav0)
            return None
        return LiuD_oJiad(v1, vq, v2)

    def handle_oString(self):
        sav0 = self.getpos()
        s = self.handle_STRING4()
        if s is None:
            self.setpos(sav0)
            return None
        return LiuD_oString(s)

    def handle_ooptgroup(self):
        sav0 = self.getpos()
        if self.handle_OpChar('[') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_oitem()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(']') is None:
            self.setpos(sav0)
            return None
        return LiuD_ooptgroup(vlst)

    def handle_oitemd(self):
        sav0 = self.getpos()
        if self.handle_OpChar('(') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_oitem()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(0)
        if not vlst:
            self.setpos(sav0)
            return None
        self.setpos(sav1)
        self.Skip(0)
        if self.handle_OpChar(')*') is None:
            self.setpos(sav0)
            return None
        return LiuD_oitemd(vlst)

    def handle_oident(self):
        sav0 = self.getpos()
        s = self.handle_OpChar('+ident')
        if s is None:
            s = self.handle_OpChar('-ident')
        if s is None:
            self.setpos(sav0)
            return None
        return LiuD_oident(s)

    def handle_onewline(self):
        sav0 = self.getpos()
        self.Skip(0)
        if self.handle_NAME('NL') is None:
            self.setpos(sav0)
            return None
        return LiuD_onewline()

    def handle_olnk(self):
        sav0 = self.getpos()
        self.Skip(0)
        if self.handle_OpChar('-') is None:
            self.setpos(sav0)
            return None
        return LiuD_olnk()

    def handle_oXlst(self):
        sav0 = self.getpos()
        self.Skip(0)
        if self.handle_OpChar('x*') is None:
            self.setpos(sav0)
            return None
        return LiuD_oXlst()

    def handle_oXchoice(self):
        sav0 = self.getpos()
        if self.handle_OpChar('x?(') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s1 = self.handle_STRING()
        if s1 is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar(',') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s2 = self.handle_STRING()
        if s2 is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_oXchoice(s1, s2)

    def handle_oXif(self):
        sav0 = self.getpos()
        if self.handle_OpChar('x?(') is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        s = self.handle_STRING()
        if s is None:
            self.setpos(sav0)
            return None
        self.Skip(0)
        if self.handle_OpChar(')') is None:
            self.setpos(sav0)
            return None
        return LiuD_oXif(s)

    def handle_oXq(self):
        sav0 = self.getpos()
        self.Skip(0)
        if self.handle_OpChar('x?') is None:
            self.setpos(sav0)
            return None
        return LiuD_oXq()

    def handle_oX(self):
        sav0 = self.getpos()
        self.Skip(0)
        if self.handle_NAME('x') is None:
            self.setpos(sav0)
            return None
        return LiuD_oX()

    def handle_protoGroup(self):
        sav0 = self.getpos()
        n = self.handle_NAME()
        if n is None:
            self.setpos(sav0)
            return None
        self.Skip(1)
        if self.handle_OpChar('{') is None:
            self.setpos(sav0)
            return None
        self.Skip(1)
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_stmt()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(1)
        self.setpos(sav1)
        self.Skip(1)
        if self.handle_OpChar('}') is None:
            self.setpos(sav0)
            return None
        return LiuD_protoGroup(n, vlst)

    def handle_Module(self):
        self.Skip(1)
        sav0 = self.getpos()
        vlst = []
        sav1 = self.getpos()
        while True:
            v3 = self.hdl_stmt()
            if v3 is None:
                break
            vlst.append(v3)
            sav1 = self.getpos()
            self.Skip(1)
        self.setpos(sav1)
        self.Skip(1)
        if self.handle_ENDMARKER() is None:
            self.setpos(sav0)
            return None
        return LiuD_Module(vlst)

def Test_Parse_LiuD(srctxt):
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


def Test_Out_LiuD(mod):
    outp = OutPrt()
    the = LiuD_out_visitor_01(outp)
    mod.walkabout(the)
    outp.newline()

s_sample_LiuD = r'''
// LiuD syntax define
// LiuTaoTao github.com/Bookaa/LiuD

.name_prefix LiuD
.set_linecomment '\/\/'
// this is comment
.set_blockcomment '/\*' '\*/'
/* comment again */

.syntax wspace

// .string STRING1 strtype1 '\$liud\$((.|\n)*?)\$duil\$'
// .string STRING2 strtype1 '\$liut\$((.|\n)*?)\$tuil\$'
// .string STRING3 strtype3 $liud$'([^'\\]*(?:\\.[^'\\]*)*)'$duil$
// .string STRING4 strtype4 $liud$'([^'\\]*(?:\\.[^'\\]*)*)'$duil$

// STRING :: STRING1 | STRING2 | STRING3

string_def : '.string' NAME NAME STRING

iExpr {
taxvalue :: ( opt2(s,vlst*) : NAME '^-' '(' strings+ ')' )
    | ( choices(vlst*) : + taxone -(crlf) ^+ '|' )
    | ( MoreDef : '+' baseitem* )
    | ( OtherSyntax : '$NewSyntax' )
    strings :: ( stringchoice(slst*) : '(' STRING ^+ '|' ')' )
        | LitString
    taxone :: ( inline : '(' stmt_tax ')' )
        | ( serie(vlst*) : + baseitem+ )
        base0 :: ( bracegroup(vlst*) : '(' base0+ ')' )
            | ( bracechoice(vlst*) : '(' base1 ^+ '|' ')' )
            | ( BoolChoice : 'Bool(' STRING ',' STRING ')' )
            | ( BoolIf : 'Bool(' STRING ')' )
            | LitName
            | LitString
            | ( ident : ('+ident' | '=ident' | '-ident')$ )
        base1 :: ( basestrn : (strings | LitName) - '$' )
            | base0
        baseitem :: ( ifnext(slst*) : '-ifnext(' STRING ^+ '|' ')' )
            | ( ifnotnext(slst*) : '-ifnotnext(' STRING ^+ '|' ')' )
            | skipdef
            | ( itemq : base1 - '?' )
            | ( itemd : base1 - '*' )
            | ( itemp : base0 - '+' )
            | ( jiad(v1,v2q?,v3q?,v4) : base0 skipdef? '^*' skipdef? base1 )
            | ( jiap(v1,v2q?,v3q?,v4) : base0 skipdef? '^+' skipdef? base1 )
            | ( optgroup(vlst*) : '[' base0+ ']' )
            | base1
            skipdef :: ( syntaxdef : '-(' - NAME - ')' )
                | ( noskip : '-' )
        LitName : NAME
        LitString : STRING
}
stmt :: stmtone NEWLINE$
    stmtone :: ( dot_syntax : '.syntax' (NAME | '-'$) )
        | ( set_linecomment : '.set_linecomment' STRING )
        | ( set_blockcomment : '.set_blockcomment' STRING STRING )
        | ( name_prefix : '.name_prefix' NAME )
        | output_rules
        | string_def
        | ( sample_text : 'Sample' 'Text' '=' STRING )
        | stmt_inline
        | stmt_tax
        | protoGroup

stmt_inline(s, vargq?, v) : NAME ['(' arg ')'] '::' taxvalue
stmt_tax(s, vq?, v) : NAME ['(' args ')'] ':' taxvalue
    args(vlst*) : arg ^+ ','
        arg(s, sq?) : NAME - ('?' | '*')$?

output_rules : 'Output' 'Rules' '{' NEWLINE$? orule* '}'

    orule(s, vlst*) : NAME ':' oitem* NEWLINE$

    oitem :: ( oJiad(v1,vq?,v2) : oX olnk? '^*' (oString | oX) )
        | ( oString : STRING4 )
        | ( ooptgroup(vlst*) : '[' oitem+ ']' )
        | ( oitemd(vlst*) : '(' oitem+ ')*' )
        | ( oident : ('+ident' | '-ident')$ )
        | ( onewline : 'NL' )
        | ( olnk : '-' )
        | ( oXlst : 'x*' )
        | ( oXchoice : 'x?(' STRING ',' STRING ')' )
        | ( oXif : 'x?(' STRING ')' )
        | ( oXq : 'x?' )
        | ( oX : 'x' )

.syntax crlf
protoGroup : NAME '{' stmt* '}'
Module(vlst*) : stmt* ENDMARKER$

Output Rules {
    MoreDef : '+' - x*
    OtherSyntax : '$NewSyntax'
    protoGroup : x '{' NL (x NL)* '}'
    opt2 : x '^-' '(' x* ')'
    choices : x ^* '\n    |'
    stringchoice : '(' x ^* '|' ')'
    inline : '(' x ')'
    serie : x*
    bracegroup : '(' x* ')'
    bracechoice : '(' x ^* '|' ')'
    BoolChoice : 'Bool(' x ',' x ')'
    BoolIf : 'Bool(' x ')'
    ident : x
    basestrn : x - '$'
    LitName : x
    LitString : x
    ifnext : '-ifnext(' x ^* '|' ')'
    ifnotnext : '-ifnotnext(' x ^* '|' ')'
    itemq : x - '?'
    itemd : x - '*'
    itemp : x - '+'
    jiad : x x? '^*' x? x
    jiap : x x? '^+' x? x
    optgroup : '[' x* ']'
    syntaxdef : '-(' - x - ')'
    noskip : '-'
    dot_syntax : '.syntax' x
    set_linecomment : '.set_linecomment' x
    set_blockcomment : '.set_blockcomment' x x
    name_prefix : '.name_prefix' x
    string_def : '.string' x x x
    sample_text : 'Sample Text =' x
    stmt_inline : x ['(' x ')'] '::' x
    stmt_tax : x ['(' x ')'] ':' x
    args : x ^* ','
    arg : x [- x]
    Module : (x NL)*
    output_rules : 'OutPut' 'Rules' '{' NL x* '}'
    orule : x ':' x* NL
    oJiad : x x? '^*' x
    oString : x
    ooptgroup : '[' x* ']'
    oitemd : '(' x* ')*'
    oident : x
    onewline : 'NL'
    olnk : '-'
    oXlst : 'x*'
    oXchoice : 'x?(' x ',' x ')'
    oXif : 'x?(' x ')'
    oXq : 'x?'
    oX : 'x'
}

Sample Text = 'hello world'

'''

if __name__ == '__main__':
    mod = Test_Parse_LiuD(s_sample_LiuD)
    if mod :
        Test_Out_LiuD(mod)
    
