# $FreeBSD$

PORTNAME=	cpr
PORTVERSION=	1.3.0
CATEGORIES=	devel www

MAINTAINER=che@bein.link
COMMENT=	Curl for People

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=curl:ftp/curl

USES=	cmake
CMAKE_OFF=	BUILD_CPR_TESTS
CMAKE_ON=	USE_SYSTEM_CURL

USE_GITHUB=	YES
GH_ACCOUNT=	whoshuu
GH_PROJECT=	googletest:googletest mongoose:mongoose
GH_TAGNAME=	${PORTVERSION} 3be1ef9:googletest df9f7a7:mongoose
GH_SUBDIR=	opt/googletest:googletest opt/mongoose:mongoose

INSTALL_TARGET=	install

.include <bsd.port.mk>
