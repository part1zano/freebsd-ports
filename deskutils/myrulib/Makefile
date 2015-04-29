# $FreeBSD$

PORTNAME=	myrulib
PORTVERSION=	0.29.16
CATEGORIES=	deskutils
MASTER_SITES=	http://lintest.ru/pub/

MAINTAINER=	alext@T7g.ORG
COMMENT=	E-Book Library Manager

LICENSE=	GPLv3

USE_GNOME=	libxml2
USE_SQLITE=	3
USE_WX=		2.8+
WX_UNICODE=	yes
WX_CONF_ARGS=	absolute
GNU_CONFIGURE=	yes
USES+=		gettext desktop-file-utils tar:bzip2
INSTALLS_ICONS=	yes

BUILD_DEPENDS=	${LOCALBASE}/gcc48:${PORTSDIR}/lang/gcc48

.include <bsd.port.mk>
