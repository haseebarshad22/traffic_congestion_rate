# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TrafficLinker
                                 A QGIS plugin
 links traffic
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-10
        copyright            : (C) 2018 by Daddy
        email                : haseebarshad22@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TrafficLinker class from file TrafficLinker.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .CongestionRate import TrafficLinker
    return TrafficLinker(iface)
