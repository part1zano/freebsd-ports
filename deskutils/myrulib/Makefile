# $FreeBSD$

PORTNAME=	myrulib
PORTVERSION=	0.29.16
CATEGORIES=	deskutils
MASTER_SITES=	http://lintest.ru/pub/

MAINTAINER=	alext@T7g.ORG
COMMENT=	E-Book Library Manager

LICENSE=	GPLv3

#USE_BZIP2=	yes
USES=	tar:bzip2
USE_GNOME=	libxml2
USE_SQLITE=	3
USE_WX=		2.8+
WX_UNICODE=	yes
WX_CONF_ARGS=	absolute
GNU_CONFIGURE=	yes
USES+=		gettext desktop-file-utils
INSTALLS_ICONS=	yes

.include <bsd.port.mk>
