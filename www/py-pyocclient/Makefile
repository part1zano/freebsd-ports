# $FreeBSD$

PORTNAME=	pyocclient
PORTVERSION=	0.1
CATEGORIES=	www python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	che@bein.link
COMMENT=	Python Owncloud client library

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE.txt

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}requests>=2.0.1:${PORTSDIR}/www/py-requests

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
