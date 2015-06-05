# $FreeBSD$

PORTNAME=	GitPython
PORTVERSION=	0.3.6
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	che@bein.link
COMMENT=	Python Git Library

LICENSE=	BSD3CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}gitdb>=0.6.4:${PORTSDIR}/devel/py-gitdb
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}nose>=1.3.4:${PORTSDIR}/devel/py-nose \
	${PYTHON_PKGNAMEPREFIX}mock>=1.0.1:${PORTSDIR}/devel/py-mock \
	${RUN_DEPENDS}

USES=		python
USE_PYTHON=	autoplist distutils

test: build
	cd ${WRKSRC} && python -m nose

.include <bsd.port.mk>
