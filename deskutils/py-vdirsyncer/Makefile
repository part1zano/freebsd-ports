# $FreeBSD: head/deskutils/py-vdirsyncer/Makefile 380909 2015-03-10 11:48:38Z robak $

PORTNAME=	vdirsyncer
PORTVERSION=	0.8.1
CATEGORIES=	deskutils python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	che@bein.link
COMMENT=	Synchronize calendars and contacts

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}atomicwrites>=0.1.4:${PORTSDIR}/devel/py-atomicwrites \
		${PYTHON_PKGNAMEPREFIX}click>=5.0:${PORTSDIR}/devel/py-click \
		${PYTHON_PKGNAMEPREFIX}click-log>=0:${PORTSDIR}/devel/py-click-log \
		${PYTHON_PKGNAMEPREFIX}click-threading>=0:${PORTSDIR}/devel/py-click-threading \
		${PYTHON_PKGNAMEPREFIX}icalendar>=3.6:${PORTSDIR}/devel/py-icalendar \
		${PYTHON_PKGNAMEPREFIX}lxml>=3.0:${PORTSDIR}/devel/py-lxml \
		${PYTHON_PKGNAMEPREFIX}requests>=2.4.3:${PORTSDIR}/www/py-requests \
		${PYTHON_PKGNAMEPREFIX}requests-toolbelt>=0.3.0:${PORTSDIR}/www/py-requests-toolbelt

USES=		python
USE_PYTHON=	autoplist distutils

.include <bsd.port.mk>
