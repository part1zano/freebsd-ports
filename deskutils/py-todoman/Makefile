# $FreeBSD$

PORTNAME=	todoman
PORTVERSION=	1.6.3
CATEGORIES=	deskutils python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	che@bein.link
COMMENT=	CalDAV-based to-do list

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}click>=6.0:devel/py-click \
		${PYTHON_PKGNAMEPREFIX}icalendar>=3.8.2:devel/py-icalendar \
		${PYTHON_PKGNAMEPREFIX}urwid>=1.2.1:devel/py-urwid \
		${PYTHON_PKGNAMEPREFIX}xdg>=0.25:devel/py-xdg \
		${PYTHON_PKGNAMEPREFIX}sqlite3>0:databases/py-sqlite3 \
		${PYTHON_PKGNAMEPREFIX}parsedatetime>0:devel/py-parsedatetime

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
