# $FreeBSD$

PORTNAME=	khal
PORTVERSION=	0.4.0
CATEGORIES=	deskutils python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	che@bein.link
COMMENT=	CalDAV-based calendar

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/COPYING

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}click>=3.2:${PORTSDIR}/devel/py-click \
	${PYTHON_PKGNAMEPREFIX}icalendar:${PORTSDIR}/devel/py-icalendar \
	${PYTHON_PKGNAMEPREFIX}urwid:${PORTSDIR}/devel/py-urwid \
	${PYTHON_PKGNAMEPREFIX}xdg:${PORTSDIR}/devel/py-xdg \
	${PYTHON_PKGNAMEPREFIX}pytz:${PORTSDIR}/devel/py-pytz \
	${PYTHON_PKGNAMEPREFIX}dateutil:${PORTSDIR}/devel/py-dateutil \
	${PYTHON_PKGNAMEPREFIX}configobj:${PORTSDIR}/devel/py-configobj \
	${PYTHON_PKGNAMEPREFIX}tzlocal>=1.0:${PORTSDIR}/devel/py-tzlocal \
	${PYTHON_PKGNAMEPREFIX}vdirsyncer:${PORTSDIR}/devel/vdirsyncer

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
