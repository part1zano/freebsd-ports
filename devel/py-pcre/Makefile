# $FreeBSD$

PORTNAME=		pcre
PORTVERSION=	0.5
CATEGORIES=		devel python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DISTNAME=		python-pcre

MAINTAINER=		che@bein.link
COMMENT=		PCRE (Perl-Compatible Regular Expressions) for Python

LICENSE=		BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENCE

RUN_DEPENDS=	pcre>=6.0:${PORTSDIR}/devel/pcre

USE_GITHUB=		yes
GH_ACCOUNT=		awahlig
GH_PROJECT=		${DISTNAME}
GH_COMMIT=		1efa30c
GH_TAGNAME=		${GH_COMMIT}

USES=			python
USE_PYTHON=		autoplist distutils

CFLAGS+=		-I${LOCALBASE}/include

.include <bsd.port.mk>
